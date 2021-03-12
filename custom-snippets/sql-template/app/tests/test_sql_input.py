import pytest
import time
from os import environ
from sqlalchemy import create_engine

DB_USER = environ['POSTGRES_USER']
DB_PASS = environ['POSTGRES_PASSWORD']
DB_HOST = environ['POSTGRES_HOST']
DB_PORT = environ['POSTGRES_PORT']
DB_NAME = environ['POSTGRES_DB']

INPUT_FILENAME = "submission.txt"

db_string = f"postgres://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
db = create_engine(db_string)

def read_student_sql():
    file = open(INPUT_FILENAME)
    line = file.read().replace("\n", " ")
    file.close()

    return line


def test_student_select_fields():
    student_sql = read_student_sql()
    result_set = db.execute(student_sql)  

    assert len(result_set) > 0, f"The SQL Query {student_sql} must return at least 1 result"

