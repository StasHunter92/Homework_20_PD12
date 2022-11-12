from flask import Flask
from flask_restx import Api

from app.database.setup_db import db
from app.views.directors_view import director_ns
from app.views.genres_view import genre_ns
from app.views.movies_view import movie_ns
from config import Config


# ----------------------------------------------------------------------------------------------------------------------
# Configurate application
def create_app(config_object) -> Flask:
    app_instance = Flask(__name__)
    app_instance.config.from_object(config_object)
    register_extensions(app_instance)
    app_instance.app_context().push()
    return app_instance


def register_extensions(app_instance: Flask):
    db.init_app(app_instance)
    api = Api(app_instance)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)


# ----------------------------------------------------------------------------------------------------------------------
# Create application instance with settings
application = create_app(Config())


# ----------------------------------------------------------------------------------------------------------------------
# Error handlers
@application.errorhandler(404)
def error_404(error):
    """Page 404 error"""
    return f"OOPS! Error {error}, page not found", 404


@application.errorhandler(500)
def error_500(error):
    """Internal server error"""
    return f"OOPS! Error {error}, server have a problem", 500


# ----------------------------------------------------------------------------------------------------------------------
# Run application
if __name__ == '__main__':
    application.run()
