/*
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
*/

const express = require("express");
const app = express();
app.use(express.json());

// Create your data structure(s) here:

// Complete the API endpoints below:

/*
POST /movies -- Add movie to the database
Request body: {
    “title”: string,
    “year”: int,
    “director”: string,
}

Response:
If valid: 201 status code and JSON {“id”: <movie id>}
If invalid: 400 status code and JSON {“error”: <message>}
If duplicate of a previous entry: 409 status code and JSON {“error”: <message>”}
*/
app.post("/movies", (req, res) => {
  res.status(501).json({ error: "Not implemented" });
});

/*
GET /movies -- Get all movies
BONUS: add query parameter to filter movies by title (e.g. /movies?title=Inception)

Response: status code 200, JSON:
{
    items: [
        { "id": 1, "title": "Inception", "year": 2010, "director": "Christopher Nolan", "rating": 4.98, "num_ratings": 5},
        …
    ]
}
*/
app.get("/movies", (req, res) => {
  res.status(501).json({ error: "Not implemented" });
});



/*
PUT /movies/{movie_id}/rating -- Recalculate movie's ratings field given new ratings, updating rating and num_rating attributes
Example path: /movies/33/rating, where 33 is a movie_id
Request body: {“ratings”: [3, 4.9, 1, 2, 4.0]}

Response:
If valid: 200 status code, JSON {“id”: <movie_id>, “rating”: <rating>, "num_ratings": <num_ratings>}
If input invalid or movie_id doesn't exist: 400 status code, JSON {“error”: <msg>)
*/
app.put("/movies/:id/rating", (req, res) => {
  res.status(501).json({ error: "Not implemented" });
});


// Starting server code, do not edit
const PORT = 5000;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
