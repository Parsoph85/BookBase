from flask import Flask
from flask import render_template

from database import db, Books, Genre

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///myBase.db'
db.init_app(app)




def input_test_data():
    """ Заполнение БД тестовыми данными. Сначала дропается вся база, потом создается новая"""

    with app.app_context():
        db.drop_all()
        db.create_all()


        horror = Genre(name="Ужасы")
        db.session.add(horror)
        adventure = Genre(name="Приключения")
        db.session.add(adventure)
        biography = Genre(name="Биография")
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
    """ Выводит список всех книг при помощи шаблонов html"""

    books = Books.query.all()
    return render_template("all_books.html", books=books)


@app.route("/genre/<int:genre_id>")
def all_books_genre(genre_id):
    """ Выводит список книг по определенному жанру"""

    genre = Genre.query.get_or_404(genre_id)
    return render_template(
        "all_books_genre.html",
        genre_name=genre.name,
        books=genre.books,
    )


if __name__ == '__main__':
    input_test_data()
    app.run()
