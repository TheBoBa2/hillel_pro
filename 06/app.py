from flask import Flask, render_template

app = Flask(__name__)

movies_db = [
    {
        "id": 1,
        "title": "Інтерстеллар",
        "genre": "Фантастика",
        "year": 2014,
        "rating": 8.7,
    },
    {
        "id": 2,
        "title": "Початок",
        "genre": "Sci-Fi / Трилер",
        "year": 2010,
        "rating": 8.8,
    },
    {
        "id": 3,
        "title": "Темний лицар",
        "genre": "Екшн / Драма",
        "year": 2008,
        "rating": 9.0,
    },
    {
        "id": 4,
        "title": "Великий Гетсбі",
        "genre": "Драма / Мелодрама",
        "year": 2013,
        "rating": 7.2,
    },
    {
        "id": 5,
        "title": "Мобі Дік",
        "genre": "Пригоди / Драма",
        "year": 2010,
        "rating": 6.2,
    },
    {
        "id": 6,
        "title": "Убити пересмішника",
        "genre": "Драма / Кримінал",
        "year": 1962,
        "rating": 8.3,
    },
    {
        "id": 7,
        "title": "Володар перснів",
        "genre": "Фентезі / Пригоди",
        "year": 2001,
        "rating": 8.8,
    },
    {
        "id": 8,
        "title": "Гаррі Поттер",
        "genre": "Фентезі / Пригоди",
        "year": 2001,
        "rating": 7.6,
    },
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/movies")
def movies():
    return render_template("items.html", movies=movies_db)


@app.route("/stats")
def stats():
    total_movies = len(movies_db)

    top_movie = max(
        movies_db,
        key=lambda x: (
            x["rating"] if isinstance(x["rating"], (int, float)) else 0
        ),
    )

    return render_template(
        "index.html",
        show_stats=True,
        total=total_movies,
        top=top_movie,
    )


if __name__ == "__main__":
    app.run(debug=True)
