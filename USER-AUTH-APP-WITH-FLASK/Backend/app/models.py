
from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable= False)
    password = db.Column(db.String(200), nullable = False)
    age = db.Column(db.Integer, nullable = False)
    role = db.Column(db.String(20), default='user')
    
    def __init__ (self, username, password,role, age):
        self.username = username
        self.password = password
        self.role = role
        self.age= age
        
    def __repr__(self):
        return f"User('{self.usernanme,self.password,self.role})"
    
    def to_dict(self):
        return {
            'id':self.id,
            'username': self.username,
            'role':self.role,
            'age':self.age
        }