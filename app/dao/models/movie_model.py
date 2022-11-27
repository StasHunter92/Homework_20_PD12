from marshmallow import Schema, fields
from sqlalchemy import ForeignKey

from app.database.setup_db import db


# ----------------------------------------------------------------------------------------------------------------------
# Create model for database
class Movie(db.Model):
    """Movie model"""
    __tablename__ = "movie"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String)
    description = db.Column(db.String)
    trailer = db.Column(db.String)
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, ForeignKey("genre.id"))
    director_id = db.Column(db.Integer, ForeignKey("director.id"))

    genre = db.relationship("Genre")
    director = db.relationship("Director")


# ----------------------------------------------------------------------------------------------------------------------
# Create schema for model
class MovieSchema(Schema):
    """Schema for Movie"""
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()
