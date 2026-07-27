import mysql.connector
from mysql.connector import pooling
import os

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            try:
                cls._instance.pool = pooling.MySQLConnectionPool(
                    pool_name="news_pool",
                    pool_size=5,
                    host=os.getenv("DB_HOST", "localhost"),
                    database=os.getenv("DB_NAME", "news_credibility_db"),
                    user=os.getenv("DB_USER", "root"),
                    password=os.getenv("DB_PASSWORD", "")
                )
            except mysql.connector.Error as e:
                print(f"Database connection pool error: {e}")
                raise e
        return cls._instance

    def get_connection(self):
        return self.pool.get_connection()
