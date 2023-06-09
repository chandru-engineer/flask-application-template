from APIs import app
import psycopg2 ##yoyo
from pandas import read_sql
from psycopg2.extras import DictCursor


class Database:
    """PostgreSQL Database class."""

    def __init__(self, DATABASE_HOST, DATABASE_USERNAME, DATABASE_PASSWORD,
                 DATABASE_PORT, DATABASE_NAME):
        self.host = DATABASE_HOST
        self.username = DATABASE_USERNAME
        self.password = DATABASE_PASSWORD
        self.port = DATABASE_PORT
        self.dbname = DATABASE_NAME
        self.conn = None

    def connect(self):
        """Connect to a Postgres database."""
        if self.conn is None:
            try:
                self.conn = psycopg2.connect(
                    host=self.host,
                    user=self.username,
                    password=self.password,
                    port=self.port,
                    dbname=self.dbname
                )
            except psycopg2.DatabaseError as error_info:
                app.logger.error(error_info)


    def select_rows_to_frame(self, query):
        """Run a SQL query to select rows from table."""
        self.connect()
        return read_sql(query, self.conn)

    def select_rows(self, query):
        """Run a SQL query to select rows from table."""
        self.connect()
        with self.conn.cursor() as cur:
            cur.execute(query)
            records = cur.fetchall()
        cur.close()
        return records

    def select_rows_fetchone(self, query):
        """Run a SQL query to select rows from table."""
        self.connect()
        with self.conn.cursor() as cur:
            cur.execute(query)
            records = cur.fetchone()
        cur.close()
        return records

    def select_rows_dict_cursor(self, query):
        """Run SELECT query and return dictionaries."""
        self.connect()
        with self.conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute(query)
            records = cur.fetchall()
        cur.close()
        return records

    def update_rows(self, query):
        """Run a SQL query to update rows in table."""
        self.connect()
        with self.conn.cursor() as cur:
            cur.execute(query)
            self.conn.commit()
            cur.close()
            return f"{cur.rowcount} rows affected."