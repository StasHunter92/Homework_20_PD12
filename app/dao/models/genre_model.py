from marshmallow import Schema, fields

from app.database.setup_db import db


# ----------------------------------------------------------------------------------------------------------------------
# Create model for database
class Genre(db.Model):
    """Genre model"""
    __tablename__ = "genre"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String)


# ----------------------------------------------------------------------------------------------------------------------
# Create schema for models
class GenreSchema(Schema):
    """Schema for Genre"""
    id = fields.Int(dump_only=True)
    name = fields.Str()
