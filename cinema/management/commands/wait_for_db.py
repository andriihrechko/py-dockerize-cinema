from django.core.management.base import BaseCommand
from django.db import connections, OperationalError
from psycopg2 import OperationalError as PsycopgError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Check database connection...")
        database_connection = None
        while not database_connection:
            try:
                database_connection = connections["default"]
            except (OperationalError, PsycopgError):
                self.stdout.write("Database unavailable, waiting 1 second...")
                from datetime import time
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database connected!"))
