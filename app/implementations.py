from app.database.setup_db import db

from app.dao.movie import MovieDAO
from app.dao.director import DirectorDAO
from app.dao.genre import GenreDAO

from app.services.movie_service import MovieService
from app.services.director_service import DirectorService
from app.services.genre_service import GenreService
# ----------------------------------------------------------------------------------------------------------------------
# MovieDAO and MovieService implementation
movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

# DirectorDAO and DirectorService implementation
director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

# GenreDAO and GenreService implementation
genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)
