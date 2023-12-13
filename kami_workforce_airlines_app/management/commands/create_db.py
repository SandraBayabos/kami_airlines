from django.core.management.base import BaseCommand
from django.db import connections, DEFAULT_DB_ALIAS, OperationalError
import psycopg2

class Command(BaseCommand):
    help = "Create the database specified in settings.py if it doesn't exist"

    def handle(self, *args, **options):
        db_settings = connections.databases[DEFAULT_DB_ALIAS]
        try:
            connections[DEFAULT_DB_ALIAS].cursor()
        except OperationalError:
            try:
                print("Database doesn't exist. Creating...")
                conn = psycopg2.connect(
                    dbname="postgres", 
                    user=db_settings['USER'],
                    password=db_settings['PASSWORD'],
                    host=db_settings['HOST'],
                )
                conn.autocommit = True
                cur = conn.cursor()
                cur.execute(f"CREATE DATABASE {db_settings['NAME']}")
                cur.close()
                conn.close()
                print("Database created!")
            except Exception as e:
                print(f"Error creating database: {e}")

