from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class Books(db.Model):
    """ Описание модели книги"""
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String, nullable=True)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id", ondelete='SET NULL'))
    genre = relationship("Genre", back_populates="books")

    def __repr__(self):
        return f"Book(fullname={self.fullname!r})"


class Genre(db.Model):
    """ Описание модели жанра"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    books = relationship(
        "Books", back_populates="genre"
    )
