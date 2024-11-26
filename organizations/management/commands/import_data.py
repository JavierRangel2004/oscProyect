# organizations/management/commands/import_data.py

from django.core.management.base import BaseCommand
from django.core.management import call_command
import os

class Command(BaseCommand):
    help = 'Import data from JSON file'

    def add_arguments(self, parser):
        parser.add_argument(
            'json_file',
            type=str,
            help='Path to the JSON file to import'
        )

    def handle(self, *args, **options):
        json_file_path = options['json_file']

        if not os.path.exists(json_file_path):
            self.stderr.write(f"File {json_file_path} does not exist.")
            return

        self.stdout.write(f"Importing data from {json_file_path}...")

        call_command('loaddata', json_file_path)

        self.stdout.write("Data import completed successfully.")
