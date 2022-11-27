from flask_restx import Resource, Namespace

from app.dao.models.genre_model import GenreSchema
from app.implementations import genre_service
# ----------------------------------------------------------------------------------------------------------------------
# Create namespace and schema instance
genre_ns = Namespace('genres')

genres_schema = GenreSchema(many=True)
genre_schema = GenreSchema()


# ----------------------------------------------------------------------------------------------------------------------
# Routes for genres
@genre_ns.route('/')
class GenresView(Resource):
    @staticmethod
    def get():
        """
        Get all genres \n
        :return: JSON response with status code 200
        """
        all_genres: list = genre_service.get_all()

        return genres_schema.dump(all_genres), 200


# ----------------------------------------------------------------------------------------------------------------------
# Routes for genre
@genre_ns.route("/<int:genre_id>")
class GenreView(Resource):
    @staticmethod
    def get(genre_id: int):
        """
        Get one genre by id \n
        :param genre_id: ID of genre
        :return: JSON response with status code 200 or 404 if genre is not found
        """
        genre: object = genre_service.get_one(genre_id)
        if not genre:
            return "Invalid id to get", 404

        return genre_schema.dump(genre), 200
