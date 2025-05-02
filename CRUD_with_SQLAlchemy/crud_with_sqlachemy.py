
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


# add new movie
@app.route('/movies/', methods = ['POST'])
def add_movie():
    data = request.json
    new_movie = Movie(title = data['title'], year = data['year'])
    db.session.add(new_movie)
    db.session.commit()
    return jsonify ({'message':'Movie Added', 'details': new_movie.to_dic()})



# get all the movies
@app.route('/movies/',methods = ['GET'])
def get_movies():
    movies = Movie.query.all()
    return jsonify([movie.to_dic() for movie in movies])



# get single movie
@app.route('/movies/<int:id>', methods = ['GET'])
def get_movie(id):
    movie = Movie.query.get(id)
    if movie:
        return movie.to_dic()
    return jsonify({'message','Movie not found'}),404


# update movie
@app.route('/movies/<int:_id>', methods = ['PUT'])
def update_movie(_id):
    movie = Movie.query.get(_id)
    if not movie:
        return jsonify ({"message": "Movie not Found"}),404
    
    data = request.json
    movie.title = data['title']
    movie.year = data['year']
    db.session.commit()
    return jsonify({"message":"Movie updated successfully", "movie": movie.to_dic()})


# delete movie
@app.route('/movies/<int:_id>', methods = ['DELETE'])
def del_movie(_id):
    movie = Movie.query.get(_id)
    if not movie:
        return jsonify ({"message":"Movie Not found"}),404
    
    db.session.delete(movie)
    db.session.commit()
    return jsonify ({"message":"Movie deleted Sucessfully"})



if __name__ == '__main__':
    app.run(debug = True)