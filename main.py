from flask import Flask
from flask import render_template

from database import db, Books, Genre

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///myBase.db'
db.init_app(app)


with app.app_context():
    db.drop_all()
    db.create_all()

    # Заполнение БД тестовыми данными
    horror = Genre(name="Horror")
    db.session.add(horror)
    adventure = Genre(name="Adventure")
    db.session.add(adventure)
    biography = Genre(name="Biography")
    db.session.add(biography)

    shining = Books(fullname="Сияние. С.Кинг", genre=horror)
    db.session.add(shining)
    ljie = Books(fullname="20000 льё под водой. Ж.Верн", genre=adventure)
    db.session.add(ljie)
    it = Books(fullname="Оно. С.Кинг", genre=horror)
    db.session.add(it)
    autobio = Books(fullname="Автобиография. А. Кристи", genre=biography)
    db.session.add(autobio)

    db.session.commit()


@app.route("/")
def all_books():
    books = Books.query.all()
    return render_template("all_books.html", books=books)


@app.route("/genre/<int:genre_id>")
def all_books_genre(genre_id):
    genre = Genre.query.get_or_404(genre_id)
    return render_template(
        "all_books_genre.html",
        genre_name=genre.name,
        books=genre.books,
    )


if __name__ == '__main__':
    app.run()