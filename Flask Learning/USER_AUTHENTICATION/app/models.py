
from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120),unique= True, nullable = False,)
    password = db.Column(db.String(120), nullable = False)
    age = db.Column(db.Integer, nullable = True)
    role = db.Column(db.String(50), nullable= False, default= 'user')
    
    
    def __init__(self, username, password,age= None, role='user'):
        self.username = username
        self.password = password
        self.role = role
        self.age = age
        
    
    def _repr_(self):
        return f'User {self.username}'
    
    
    def to_dic(self):
        return {
            "id": self.id,
            "Name": self.username,
            "role" : self.role,
            "age": self.age
        }
    