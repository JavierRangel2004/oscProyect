# organizations/management/commands/import_data.py

import re
import os
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from organizations.models import Organization, Category
from projects.models import Project
from django.db import transaction
import shlex
from io import StringIO

class Command(BaseCommand):
    help = 'Importa datos desde un volcado SQL de MySQL a la base de datos de Django'

    def add_arguments(self, parser):
        parser.add_argument(
            'sql_file',
            type=str,
            help='Ruta al archivo SQL de volcado de MySQL'
        )

    def handle(self, *args, **options):
        sql_file_path = options['sql_file']

        if not os.path.exists(sql_file_path):
            raise CommandError(f"El archivo {sql_file_path} no existe.")

        self.stdout.write(self.style.NOTICE('Iniciando la importación de datos...'))

        with open(sql_file_path, 'r', encoding='utf-8') as file:
            sql_content = file.read()

        # Extraer las inserciones de cada tabla
        sector_data = self.extract_insert_data(sql_content, 'sector')
        organizacion_data = self.extract_insert_data(sql_content, 'organizacion')
        programa_data = self.extract_insert_data(sql_content, 'programa')

        with transaction.atomic():
            # Importar Sectores como Categorías
            self.import_sectors(sector_data)

            # Importar Organizaciones
            self.import_organizations(organizacion_data)

            # Importar Programas como Proyectos
            self.import_programs(programa_data)

        self.stdout.write(self.style.SUCCESS('Importación completada exitosamente.'))

    def extract_insert_data(self, sql_content, table_name):
        """
        Extrae los valores de las sentencias INSERT para una tabla específica.
        """
        pattern = rf"INSERT INTO `{table_name}` .*? VALUES\s*(.*?);"
        matches = re.findall(pattern, sql_content, re.DOTALL)
        if not matches:
            self.stdout.write(self.style.WARNING(f"No se encontraron datos para la tabla `{table_name}`."))
            return []

        # Unir todas las inserciones en una sola cadena
        all_values = ''.join(matches)

        # Dividir por "),(" para separar los registros
        records = re.split(r'\),\s*\(', all_values.strip('();\n '))

        data = []
        for record in records:
            # Agregar paréntesis que fueron removidos
            if not record.startswith('('):
                record = '(' + record
            if not record.endswith(')'):
                record = record + ')'
            fields = self.parse_record(record)
            data.append(fields)

        return data

    def parse_record(self, record):
        """
        Parses a record line from an SQL INSERT and returns a list of values.
        """
        # Replace 'NULL' with None
        record = record.replace("NULL", "None")
        # Use shlex to split the record
        try:
            lexer = shlex.shlex(record, posix=True)
            lexer.whitespace = ','
            lexer.whitespace_split = True
            lexer.quotechars = "'"
            lexer.escape = '\\'
            fields = list(lexer)
            # Remove leading/trailing parentheses from first and last fields
            if fields[0].startswith('('):
                fields[0] = fields[0][1:]
            if fields[-1].endswith(')'):
                fields[-1] = fields[-1][:-1]
            fields = [field if field != 'None' else None for field in fields]
            return fields
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error parsing record {record}: {e}'))
            return []

    def import_sectors(self, sectors):
        """
        Importa los sectores como categorías en el modelo Category.
        """
        self.stdout.write(self.style.NOTICE('Importando Sectores como Categorías...'))
        for sector in sectors:
            try:
                id_sector = int(sector[0].strip())
                sector_nombre = sector[1].strip()
                category, created = Category.objects.get_or_create(
                    id=id_sector,
                    defaults={'name': sector_nombre}
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Categoría creada: {sector_nombre}'))
            except Exception as e:
                self.stderr.write(self.style.ERROR(f'Error al importar sector {sector}: {e}'))

    def import_organizations(self, organizations):
        """
        Importa las organizaciones desde la tabla `organizacion`.
        """
        self.stdout.write(self.style.NOTICE('Importando Organizaciones...'))
        for org in organizations:
            if not org:
                continue  # Saltar registros que no se pudieron parsear
            try:
                self.stdout.write(f'Importando organización: {org}')

                id_org = int(org[0])
                nombre_org = org[1].strip()
                id_sector = int(org[2])
                ubicacion = org[3].strip()
                redes_sociales_1 = org[4].strip() if org[4] else None
                redes_sociales_2 = org[5].strip() if org[5] else None
                pagina_web = org[6].strip() if org[6] else None
                telefono = str(org[7]).strip() if org[7] else None
                correo = org[8].strip() if org[8] else None

                # Obtener la categoría correspondiente
                try:
                    category = Category.objects.get(id=id_sector)
                except Category.DoesNotExist:
                    self.stderr.write(self.style.ERROR(f'Categoría con ID {id_sector} no existe para la organización {nombre_org}.'))
                    continue

                organization, created = Organization.objects.update_or_create(
                    id=id_org,  # Asumiendo que el campo `id` en Django coincide con `ID_Organizacion`
                    defaults={
                        'name': nombre_org,
                        'address': ubicacion,
                        'social_media_1': redes_sociales_1,
                        'social_media_2': redes_sociales_2,
                        'website': pagina_web,
                        'phone_number': telefono,
                        'email': correo,
                        'is_active': True,  # Puedes ajustar según tus necesidades
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Organización creada: {nombre_org}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Organización actualizada: {nombre_org}'))

                # Asignar la categoría
                organization.categories.add(category)

            except Exception as e:
                self.stderr.write(self.style.ERROR(f'Error al importar organización {org}: {e}'))

    def import_programs(self, programs):
        """
        Importa los programas como proyectos en el modelo Project.
        """
        self.stdout.write(self.style.NOTICE('Importando Programas como Proyectos...'))
        for prog in programs:
            try:
                id_programa = int(prog[0].strip())
                nombre_programa = prog[1].strip()
                id_organizacion = int(prog[2].strip())

                # Obtener la organización correspondiente
                try:
                    organization = Organization.objects.get(id=id_organizacion)
                except Organization.DoesNotExist:
                    self.stderr.write(self.style.ERROR(f'Organización con ID {id_organizacion} no existe para el programa {nombre_programa}.'))
                    continue

                project, created = Project.objects.update_or_create(
                    name=nombre_programa,
                    organization=organization,
                    defaults={
                        'description': '',  # Puedes ajustar o dejar en blanco
                        'objectives': '',
                        'achievements': '',
                        'participation_methods': '',
                        'is_active': True,
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Proyecto creado: {nombre_programa}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Proyecto actualizado: {nombre_programa}'))

            except Exception as e:
                self.stderr.write(self.style.ERROR(f'Error al importar programa {prog}: {e}'))