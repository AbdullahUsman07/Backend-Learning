
from flask import Flask, jsonify, request

app = Flask(__name__)

movies = []

@app.route('/movies', methods = ['POST'])
def add_movies():
    data = request.get_json()
    movies.append(data)
    return jsonify({"message": "Movie Added Sucessfully", "movie": data}),201


@app.route('/movies', methods = ['GET'])
def get_movies():
    return jsonify(movies)

@app.route('/movies/<int:index>', methods = ['GET'])
def get_movie_by_index(index):
    if 0 <= index < len(movies):
        return jsonify(movies[index])
    
    else:
        return jsonify({'Error' : 'Movie Not Found'}),404
    

@app.route('/movies/<int:index>', methods = ['PUT'])
def update_movie(index):

    if 0 <= index < len(movies):
       data = request.get_json()
       movies[index] =data
       return jsonify({'message': 'Movie Updated Sucessfully'})
    
    else:
        return jsonify({"message': 'can't find new movie"}), 404
    

@app.route('/movies/<int:index>', methods = 'DELETE')
def delete_movie(index):
    if 0 <= index < len(movies):
      movies.remove(index)
      return jsonify({"message": "Movie Deleted Successfully"})
    
    else:
        return jsonify({"message": "Can't delete movie"})


if __name__ == '__main__':
    app.run(debug = True)