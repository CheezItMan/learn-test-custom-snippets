import pytest
import time
from os import environ
import sqlalchemy
from sqlalchemy import create_engine

# DB_USER = environ['POSTGRES_USER']
# DB_PASS = environ['POSTGRES_PASSWORD']
# DB_HOST = environ['POSTGRES_HOST']
# DB_PORT = environ['POSTGRES_PORT']
# DB_NAME = environ['POSTGRES_DB']

DB_NAME = 'database'
DB_USER = 'username'
DB_PASS = 'secret'
DB_HOST = 'db'
DB_PORT = '5432'

INPUT_FILENAME = "submission.txt"

db_string = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# Testing
# db_string = f"postgresql://postgres:@localhost:5432/docker"
db = create_engine(db_string)

def teardown_module(module):
    db.execute(f"DROP SCHEMA public CASCADE;")
    db.execute("CREATE SCHEMA public;")

def setup_module(module):
    db.execute(f"DROP SCHEMA public CASCADE;")
    db.execute("CREATE SCHEMA public;")
    db.execute(f"GRANT ALL ON SCHEMA public TO {DB_USER};")
    db.execute(f"GRANT ALL ON SCHEMA public TO public;")

def read_student_sql():
    file = open(INPUT_FILENAME)
    line = file.read().replace("\n", " ")
    file.close()

    return line

def test_can_can_create_drivers_table():
    student_sql = read_student_sql()

    try:
        result_set = db.execute(student_sql)
    except sqlalchemy.exc.OperationalError: 
        pytest.fail(f"SQL statement fails {student_sql}")

    try:  

        # Check if table exists
        rs = db.execute("SELECT EXISTS(  SELECT * FROM information_schema.tables WHERE table_schema='public' AND table_name='drivers');")
        for row in rs:
            assert row[0], f"Drivers table not created with {student_sql}"
    except:
        pytest.fail("Drivers table not created")
