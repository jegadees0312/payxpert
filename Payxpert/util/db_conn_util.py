
import mysql.connector
from exceptions.custom_exceptions import DatabaseConnectionException

class DBConnUtil:
    @staticmethod
    def get_connection():
        try:
            connection = mysql.connector.connect(
                host="localhost",
                database="payxpert",
                user="root",
                password="root",port="3306"
            )
            return connection
        except mysql.connector.Error as e:
            raise DatabaseConnectionException("Failed to connect to database")