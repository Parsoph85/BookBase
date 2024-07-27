from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String, nullable=True)
    added = db.Column(db.DateTime, nullable=False, default=func.now())

    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id", ondelete='SET NULL'))
    genre = relationship("Genre", back_populates="books")

    def __repr__(self):
        return f"Book(fullname={self.fullname!r})"


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    employees = relationship(
        "Book", back_populates="genre"
    )
