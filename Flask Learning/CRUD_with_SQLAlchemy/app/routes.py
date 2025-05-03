from flask import Blueprint, jsonify, request
from .models import Movie
from . import db


movies_bp = Blueprint('movies',__name__)

@movies_bp.route('/')
def home():
    return "Flask App with Blueprints Running"

@movies_bp.route('/movies', methods = ['POST'])
def add_movie():
    data = request.json
    new_movie = Movie(title = data['title'], year = data['year'],description= data['description'])
    db.session.add(new_movie)
    db.session.commit()
    return jsonify ({"message":"Movie Added", "movie": new_movie.to_dic()})


@movies_bp.route('/movies', methods = ['GET'])
def get_movies():
    movies = Movie.query.all()
    return jsonify([movie.to_dic() for movie in movies])


@movies_bp.route('/movies/<int:_id>', methods = ['GET'])
def get_movie(_id):
    movie = Movie.query.get(_id)
    if movie:
        return jsonify(movie.to_dic())
    return jsonify({"message":"Movies Not Found"})


@movies_bp.route('/movies/<int:_id>', methods = ['PUT'])
def update_movie(_id):
    movie = Movie.query.get(_id)
    if not movie:
        return jsonify ({"message":"No movie found"}),404
    data = request.json
    movie.title = data['title']
    movie.year = data['year']
    movie.description = data['description']
    db.session.commit()
    return jsonify ({"message": "Movie Update Sucessful", "movie": movie.to_dic()})

@movies_bp.route('/movies/<int:_id>', methods = ['DELETE'])
def delete_movie(_id):
    movie = Movie.query.get(_id)
    if not movie:
        return jsonify ({"message": "Movie not found"}), 404
    db.session.delete(movie)
    db.session.commit()
    return jsonify({"message": "Movie deleted Successfully"})

