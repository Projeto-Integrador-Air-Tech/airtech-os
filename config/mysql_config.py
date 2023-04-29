import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

class MySQLConnection:
    """
    A class used to create a MySQL connection object in Python, using the `mysql.connector` package.
    It reads the database credentials from environment variables using the `dotenv` package.
    """
    
    def __init__(self):
        """
        Creates a new `MySQLConnection` object.
        """
        self._host = os.getenv('MYSQL_HOST')
        self._user = os.getenv('MYSQL_USER')
        self._password = os.getenv('MYSQL_PASSWORD')
        self._database = os.getenv('MYSQL_DATABASE')
        self._port = os.getenv('MYSQL_PORT')
        self._conn = None
    
    def __enter__(self):
        """
        Establishes a MySQL database connection using the credentials stored in environment variables.
        Returns the database connection object.
        """
        try:
            self._conn = mysql.connector.connect(
                host=self._host,
                user=self._user,
                password=self._password,
                database=self._database,
                port=self._port
            )
        except mysql.connector.Error as err:
            print(f"Error connecting to MySQL: {err}")
            raise err
        return self._conn
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Closes the MySQL database connection when the connection is no longer needed.
        """
        if exc_type:
            print(f"Error: {exc_type}, {exc_val}")
        if self._conn:
            self._conn.close()
