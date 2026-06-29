import sqlite3
import os


def get_db_connection():
    print("DATABASE PATH =", os.path.abspath("mentorconnect.db"))

    conn = sqlite3.connect("mentorconnect.db")
    conn.row_factory = sqlite3.Row
    return conn