import os
import psycopg2
from psycopg2 import pool
import psycopg2.pool

from dotenv import load_dotenv

load_dotenv()

class DatabaseConnectionPool:

    """
     this class manages a pool of PostgreSQL database connections using the psycopg2 library
     instead of opening and closing database connection everytime they are needed this class
     creates a connection pool(up to 10 connection pools) from which we can access a connection object and manually destory it

     the db credentials are stored in environment variables for security purposes
    """

    def __init__(self):
        self.db_host = os.environ.get('DB_HOST')
        self.db_user = os.environ.get('DB_USER')
        self.db_password = os.environ.get('DB_PASSWORD')
        self.db_name = os.environ.get('DB_NAME')
        self.connection_pool = None
    
    def get_connection_pool(self):
        if self.connection_pool is None:
            connection_string = f"host={self.db_host} user={self.db_user} password={self.db_password} dbname={self.db_name}"
            self.connection_pool = psycopg2.pool.SimpleConnectionPool(1,10,connection_string)
        return self.connection_pool
    
    def get_connection(self):
        try:
            pool = self.get_connection_pool()
            conn = pool.getconn()
            return conn
        except psycopg2.Error as e:
            print("Error while getting connection from pool: ", e)
            return None

    
    def release_connection(self,conn):
        if conn:
            try:
                pool = self.get_connection_pool()
                pool.putconn(conn)
            except psycopg2.Error as e:
                print("Eror while releasing connection back to the pool: ",e)
        
    def reset_connection_pool(self):
        if self.connection_pool:
            self.connection_pool.closeall()
        self.connection_pool = None

db_connection_pool = DatabaseConnectionPool()