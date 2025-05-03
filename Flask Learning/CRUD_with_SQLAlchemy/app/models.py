
from . import db

class Movie(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    year = db.Column(db.Integer, nullable = False)
    description = db.Column(db.String(250),nullable = False)

    def __init__(self,title,year,description):
        self.title = title
        self.year= year
        self.description = description


    def to_dic(self):
        return {
            "id": self.id,
            "title": self.title,
            "year": self.year,
            "description": self.description
        }
 