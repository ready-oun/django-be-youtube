from django.db import connections 
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand
import time 

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for DB Connections...")

        is_db_connected = None 

        while not is_db_connected:
            try:
                is_db_connected = connections['default']
            except(OperationalError):
                self.stdout.write("Connection Trying...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('PostgreSQL Connections Success'))

