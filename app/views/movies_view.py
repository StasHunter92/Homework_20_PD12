from flask import request
from flask_restx import Resource, Namespace
from marshmallow import ValidationError

from app.dao.models.movie_model import MovieSchema
from app.implementations import movie_service
# ----------------------------------------------------------------------------------------------------------------------
# Create namespace and schema instance
movie_ns = Namespace('movies')

movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()


# ----------------------------------------------------------------------------------------------------------------------
# Routes for movies
@movie_ns.route('/')
class MoviesView(Resource):
    @staticmethod
    def get():
        """
        Get all movies \n
        :return: JSON response with status code 200
        """
        data: dict = {
            "director_id": request.args.get("director_id"),
            "genre_id": request.args.get("genre_id"),
            "year": request.args.get("year")
        }

        all_movies: list = movie_service.get_all(data)

        return movies_schema.dump(all_movies), 200

    @staticmethod
    def post():
        """
        Create a new movie \n
        :return: JSON response with status code 201 or 500 request body is wrong
        """
        data = request.json

        try:
            serialized_book: dict = movie_schema.load(data)
        except ValidationError:
            return "Invalid fields", 500

        location: str = movie_service.create(serialized_book)

        return f"New movie {location} created", 201, {"Location": location}


# ----------------------------------------------------------------------------------------------------------------------
# Routes for movie
@movie_ns.route("/<int:movie_id>")
class MovieView(Resource):
    @staticmethod
    def get(movie_id: int):
        """
        Get one movie by id \n
        :param movie_id: ID of movie
        :return: JSON response with status code 200 or 404 if movie is not found
        """
        movie: object = movie_service.get_one(movie_id)

        if not movie:
            return "Invalid id to get", 404

        return movie_schema.dump(movie), 200

    @staticmethod
    def put(movie_id: int):
        """
        Update movie information by id \n
        :param movie_id: ID of movie
        :return: No content response 204 or 404 if movie is not found
        """
        data = request.json
        data['id'] = movie_id
        movie: object = movie_service.get_one(movie_id)

        if not movie:
            return "Invalid id to update", 404

        movie_service.update(data)

        return "", 204

    @staticmethod
    def delete(movie_id: int):
        """
        Delete movie by id \n
        :param movie_id: ID of movie
        :return: No content response 204 or 404 if movie is not found
        """
        movie: object = movie_service.get_one(movie_id)

        if not movie:
            return "Invalid id to delete", 404

        movie_service.delete(movie_id)

        return "", 204
