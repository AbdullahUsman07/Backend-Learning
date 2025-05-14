
import mysql.connector

def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="*********",  
            database="hostel_management"
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def close_db(conn):
    if conn:
        conn.close()
