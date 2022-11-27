import pytest

from unittest.mock import MagicMock

from app.dao.director import DirectorDAO
from app.dao.genre import GenreDAO
from app.dao.movie import MovieDAO
from app.test.conftest.test_data.director_data import ALL_DIRECTORS, ONE_DIRECTOR
from app.test.conftest.test_data.genre_data import ALL_GENRES, ONE_GENRE
from app.test.conftest.test_data.movie_data import ALL_MOVIES, ONE_MOVIE, CREATE_MOVIE


# ----------------------------------------------------------------------------------------------------------------------
# Mocked fixture for movie dao
@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)
    movie_dao.get_all = MagicMock(return_value=ALL_MOVIES)
    movie_dao.get_one = MagicMock(return_value=ONE_MOVIE)
    movie_dao.create = MagicMock(return_value=CREATE_MOVIE)
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()
    return movie_dao


# ----------------------------------------------------------------------------------------------------------------------
# Mocked fixture for director dao
@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)
    director_dao.get_all = MagicMock(return_value=ALL_DIRECTORS)
    director_dao.get_one = MagicMock(return_value=ONE_DIRECTOR)
    return director_dao


# ----------------------------------------------------------------------------------------------------------------------
# Mocked fixture for genre dao
@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)
    genre_dao.get_all = MagicMock(return_value=ALL_GENRES)
    genre_dao.get_one = MagicMock(return_value=ONE_GENRE)
    return genre_dao
