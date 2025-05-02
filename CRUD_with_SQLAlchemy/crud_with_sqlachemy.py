
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

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
    

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "Api with SQLAlchemy"

@app.route('/movies/', methods = ['POST'])
def add_movie():
    data = request.json
    new_movie = Movie(title = data['title'], year = data['year'])
    db.session.add(new_movie)
    db.session.commit()
    return jsonify ({'message':'Movie Added', 'details': new_movie.to_dic()})



if __name__ == '__main__':
    app.run(debug = True)