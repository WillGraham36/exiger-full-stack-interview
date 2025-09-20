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
    "num_ratings": int (>= 0)
}

To run:
1. cd flask
2. flask run OR python -m flask run
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Create your data structure(s) here:

# Complete the API endpoints below:

"""
POST /movies -- Add movie to the database
Request body: {
    “title”: string,
    “year”: int,
    “director”: string
}

Response:
If valid: 201 status code and JSON {“id”: <movie id>}
If invalid: 400 status code and JSON {“error”: <message>}
If duplicate of a previous entry: 409 status code and JSON {“error”: <message>”}
"""
# TODO: add route decorator
def add_movie():
    pass

"""
GET /movies -- Get all movies
BONUS: add query parameter to filter movies by title (e.g. /movies?title=Inception)

Response: status code 200, JSON: 
{ 
    items: [
        { "id": 1, "title": "Inception", "year": 2010, "director": "Christopher Nolan", "rating": 4.98, "num_ratings": 5},
        …
    ]
}
"""
# TODO: add route decorator
def get_movies():
    pass
