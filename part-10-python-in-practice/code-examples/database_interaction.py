# database_interaction.py

import sqlite3

def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)

    return conn

def create_table(conn):
    """ Create a table in the provided database connection """
    try:
        cursor = conn.cursor()
        cursor.execute(""" CREATE TABLE IF NOT EXISTS projects (
                            id integer PRIMARY KEY,
                            name text NOT NULL,
                            start_date text,
                            end_date text
                          ); """)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def insert_project(conn, project):
    """ Insert a new project into the projects table """
    try:
        cursor = conn.cursor()
        cursor.execute(""" INSERT INTO projects(name, start_date, end_date)
                           VALUES(?,?,?) """, project)
        conn.commit()
        return cursor.lastrowid
    except sqlite3.Error as e:
        print(e)

def main():
    database = "example.db"

    # create a database connection
    conn = create_connection(database)

    if conn is not None:
        # create projects table
        create_table(conn)

        # insert project
        project = ('Cool App', '2021-01-01', '2021-12-31')
        project_id = insert_project(conn, project)

        # query all projects
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM projects")

        rows = cursor.fetchall()

        for row in rows:
            print(row)

        # close connection
        conn.close()
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
