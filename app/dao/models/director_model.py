from marshmallow import Schema, fields

from app.database.setup_db import db


# ----------------------------------------------------------------------------------------------------------------------
# Create model for database
class Director(db.Model):
    """Director model"""
    __tablename__ = "director"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String)


# ----------------------------------------------------------------------------------------------------------------------
# Create schema for model
class DirectorSchema(Schema):
    """Schema for Director"""
    id = fields.Int(dump_only=True)
    name = fields.Str()
