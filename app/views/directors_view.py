from flask_restx import Resource, Namespace

from app.dao.models.director_model import DirectorSchema
from app.implementations import director_service
# ----------------------------------------------------------------------------------------------------------------------
# Create namespace and schema instance
director_ns = Namespace('directors')

directors_schema = DirectorSchema(many=True)
director_schema = DirectorSchema()


# ----------------------------------------------------------------------------------------------------------------------
# Routes for directors
@director_ns.route('/')
class DirectorsView(Resource):
    @staticmethod
    def get():
        """
        Get all directors

        :return: JSON response with status code 200
        """
        all_directors: list = director_service.get_all()

        return directors_schema.dump(all_directors), 200


# ----------------------------------------------------------------------------------------------------------------------
# Routes for director
@director_ns.route("/<int:director_id>")
class DirectorView(Resource):
    @staticmethod
    def get(director_id: int):
        """
        Get one director by id

        :param director_id: ID of director
        :return: JSON response with status code 200 or 404 if director is not found
        """
        director: object = director_service.get_one(director_id)
        if not director:
            return "Invalid id to get", 404

        return director_schema.dump(director), 200
