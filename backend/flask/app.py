"""
To run:
1. cd flask
2. flask run OR python -m flask run
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

"""
We are building a movie database and need to complete a couple of API endpoints
We won't connect to a real database here, so we want you to create a data structure to mimic one

Movies have the following attributes:
{
    "id": int,
    "title": string,
    "year": int,
    "director": string,
    "rating": float (1-5 inclusive),
    "genre": string (must be one of: action, horror, drama, sci-fi)
}
"""

# Create your data structure(s) here:

# Complete the API endpoints below:

"""
Add movie to the database
Request body: {
    “title”: string,
    “year”: int,
    “director”: string,
    “rating”: float (1-5 inclusive)
    “genre”: string (must be one of: action, horror, drama, sci-fi)
}

Response:
If valid: 201 status code and JSON {“id”: <movie id>}
If invalid: 400 status code and JSON {“error”: <message>}
If duplicate of a previous entry: return 409 status code and JSON {“error”: <message>”}
"""
@app.route('/movies', methods=['POST'])
def add_movie():
    return 400, jsonify({})

"""
Get all movies
BONUS: add query parameter filter movies by title

Response: status code 200, JSON: 
{
  { "id": 1, "title": "Inception", "year": 2010, "director": "Christopher Nolan", "genre": "Sci-Fi", rating: 4.98},
  …
}
"""
@app.route('/movies', methods=['GET'])
def get_movies():
    return 400, jsonify({})

"""
Update movie rating
Request body:
{
  “ratings”: [3, 4.9, 1, 2, 4.0]
}

Response:
If valid: 200 status code, JSON {“id”: <movie_id>, “rating”: <rating>}
If input invalid: 400 status code, JSON {“error”: <msg>)
"""
@app.route('/movies/<movie_id>/rating', methods=['PUT'])
def update_rating(movie_id):
    return 400, jsonify({})