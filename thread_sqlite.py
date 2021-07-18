import sqlite3
import os

BASE_DIR = os.path.dirname(__file__)
DATA_FILE = BASE_DIR + '/data/test.sqlite3'

def open_db():
    conn = sqlite3.connect(DATA_FILE)
    conn.row_factory = dict_factory
    return conn

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def exec(sql, *args):
    db = open_db()
    c = db.cursor()
    c.execute(sql, args)
    db.commit()
    return c.lastrowid


def select_injection(injection):
    db = open_db()
    c = db.cursor()
    c.execute('SELECT * FROM test WHERE user_name="' + injection + '"')
    return c.fetchall()