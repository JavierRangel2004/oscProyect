# organizations/management/commands/export_data.py

from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Export data to a JSON file'

    def add_arguments(self, parser):
        parser.add_argument(
            'output_file',
            type=str,
            help='Output file path'
        )

    def handle(self, *args, **options):
        output_file = options['output_file']
        with open(output_file, 'w', encoding='utf-8') as f:
            call_command('dumpdata', '--natural-foreign', '--natural-primary', '--indent', '2', stdout=f)
        self.stdout.write(self.style.SUCCESS(f'Data exported to {output_file}'))
