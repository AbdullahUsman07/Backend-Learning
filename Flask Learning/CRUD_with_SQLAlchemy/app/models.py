
from . import db

class Movie(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    year = db.Column(db.Integer, nullable = False)

    def __init__(self,title,year):
        self.title = title
        self.year= year

    def to_dic(self):
        return {
            "id": self.id,
            "title": self.title,
            "year": self.year
        }
 