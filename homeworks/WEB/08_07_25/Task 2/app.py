from flask import Flask, render_template, abort, redirect, url_for
import random

app = Flask(__name__)

movies = {
    "Superman": {
        "id": 1,
        "description": "Superman must reconcile his alien Kryptonian heritage with his human upbringing as reporter Clark Kent..."
    },
    "I Know What You Did Last Summer": {
        "id": 2,
        "description": "A group of friends are terrorised by a stalker who knows about a gruesome incident from their past."
    },
    "Jurassic World: Rebirth": {
        "id": 3,
        "description": "Five years post-Jurassic World: Dominion (2022), an expedition braves isolated equatorial regions to extract DNA from three massive prehistoric creatures for a groundbreaking medical breakthrough."
    },
    "F1: The Movie": {
        "id": 4,
        "description": "A Formula One driver comes out of retirement to mentor and team up with a younger driver."
    },
    "Sinners": {
        "id": 5,
        "description": "Trying to leave their troubled lives behind, twin brothers return to their hometown to start again, only to discover that an even greater evil is waiting to welcome them back."
    }
}


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/movie/<int:id>/")
def movie(id):
    movie_title = None
    for title, info in movies.items():
        if info["id"] == id:
            movie_title = title
            movie_description = info["description"]
            
    if movie_title:
        return render_template("movie.html", movie_title=movie_title, movie_description=movie_description)
    else:
        abort(404)

@app.route("/random/")
def random_movie():
    random_id = random.randint(1, 5)
    return redirect(url_for('movie', id=random_id))

if __name__ == "__main__":
    app.run(debug=True)