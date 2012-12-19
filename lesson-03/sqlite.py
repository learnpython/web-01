#!/usr/bin/env python

import os
import sqlite3


DIRNAME = os.path.abspath(os.path.dirname(__file__))
rel = lambda *parts: os.path.abspath(os.path.join(DIRNAME, *parts))

DATABASE_NAME = rel('learnpython.db')


def create_tables(cursor):
    """
    Create necessary tables if they don't exist in database.
    """
    try:
        cursor.execute("""
        CREATE TABLE lessons (
            number INTEGER PRIMARY KEY,
            title TEXT NOT NULL
        );
        """)

        cursor.execute("""
        CREATE TABLE students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        );
        """)
    except sqlite3.OperationalError:
        cursor.connection.rollback()
        return False

    cursor.connection.commit()
    return True


def insert_data(cursor):
    """
    Insert initial data.
    """
    # Lessons
    lessons = (
        (1, 'Python standard library'),
        (2, 'Bootstrap project'),
        (3, 'WSGI & DB-API'),
    )
    cursor.executemany('INSERT INTO lessons VALUES (?, ?);', lessons)

    # Students
    students = (
        (1, 'Alexandr Kobzar', 'maodzedun@gmail.com'),
        (2, 'Ivan Tolkach', 'ivan@tolkach.com'),
        (3, 'Sergey Smirnov', 'smirnoffs@gmail.com'),
        (4, 'Maksym Klymyshyn', 'klymyshyn@gmail.com'),
        (5, 'Maria Bochkovskaya', 'maria@zakaz.ua'),
        (6, 'Valentine Makukhina', 'refreshka@gmail.com'),
    )
    cursor.executemany('INSERT INTO students VALUES (?, ?, ?)', students)

    # If we don't commit data, they will unavailable at next run
    cursor.connection.commit()


def main():
    # Create database connection and get cursor object
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    # Create necessary tables if they don't exist
    created = create_tables(cursor)

    # Insert initial data if tables just created
    if created:
        insert_data(cursor)

    # Read data from tables and show results in CSV format
    print_rows(select_data(cursor))
    print_rows(select_data(cursor, 'gmail.com'))
    print_rows(select_data(cursor, '%gmail.com'))


def print_rows(rows):
    """
    Print rows in CSV format if any data available.
    """
    if rows:
        for i, row in enumerate(rows):
            if i == 0:
                print(','.join(row.keys()))
            print(','.join(map(unicode, row)))
    else:
        print('No data available.')
    print


def select_data(cursor, email=None):
    """
    Select data from students table.
    """
    if email:
        cursor.execute('SELECT * FROM students WHERE email LIKE ?', [email])
    else:
        cursor.execute('SELECT * FROM students;')
    return cursor.fetchall()


if __name__ == '__main__':
    main()
