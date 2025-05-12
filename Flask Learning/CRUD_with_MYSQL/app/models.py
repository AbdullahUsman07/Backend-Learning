from flask import jsonify
from app.db import mysql

class User:
    @staticmethod
    def get_all_users():
        curr = mysql.connection.cursor()
        curr.execute("Select * from Users")
        users = curr.fetch_all()
        curr.close()
        return users
    
    @staticmethod
    def get_user(user_id):
        curr = mysql.connection.cursor()
        curr.execute("Select * from Users where id = %s",(user_id))
        user = curr.fetch_all()
        curr.close()
        return user 
    
    @staticmethod
    def create_user(name, email, phone):
        curr = mysql.connection.cursor()
        
        try:
            curr.execute("Insert into Users (name, email, phone) values (%s, %s, %s) ",(name, email, phone))
            mysql.connection.commit()
            userid = curr.lastrowid
            return userid
        except Exception as e:
            mysql.connect.rollback()
            raise e
        finally:
            curr.close()
        
    @staticmethod
    def update_user(user_id, name, email, phone):
        curr = mysql.connection.cursor()
        curr.execute("Update Users SET name = %s, email = %s, phone = %s where id = %s", (name, email, phone, user_id))
        mysql.connection.commit()
        curr.close()
        
    @staticmethod
    def delete_user(user_id):
        curr = mysql.connection.cursor
        curr.execute("Delete from Users where id = %s", (user_id))
        mysql.connection.commit()
        curr.close()
            