import pytest

from app.services.movie_service import MovieService
from app.test.conftest.conftest import movie_dao


# ----------------------------------------------------------------------------------------------------------------------
# Test class for movie service
class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao: movie_dao):
        """
        Create a test movie service \n
        :param movie_dao: Mocked movie dao
        """
        self.movie_service = MovieService(movie_dao)

    def test_get_all(self):
        movies = self.movie_service.get_all({})
        assert movies is not None, "Failed to get movies from database"
        assert len(movies) > 0, "Empty list of movies"

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None, "Failed to get movie from database"
        assert movie.id == 1, "Wrong movie id"
        assert movie.title == "Test title 1", "Wrong movie title"

    def test_create(self):
        data = {"id": 3, "title": "Test Movie"}
        location = self.movie_service.create(data)

        assert location is not None, "Failed co create new movie"
        assert type(location) is str, "Returned value is not a string"
        assert location == "/movies/3", "Wrong location"

    def test_update(self):
        data = {"id": 3,
                "title": "Test title 3",
                "description": "Test description 3",
                "trailer": "Test trailer 3",
                "year": 2010,
                "rating": 3.0,
                "genre_id": 3,
                "director_id": 3}
        assert self.movie_service.update(data) is None, "Something returned"

    def test_delete(self):
        assert self.movie_service.delete(1) is None, "Something returned"
