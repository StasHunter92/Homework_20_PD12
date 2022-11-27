import pytest

from app.services.genre_service import GenreService
from app.test.conftest.conftest import genre_dao


# ----------------------------------------------------------------------------------------------------------------------
# Test class for genre service
class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao: genre_dao):
        """
        Create a test genre service \n
        :param genre_dao: Mocked genre dao
        """
        self.genre_service = GenreService(genre_dao)

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert genres is not None, "Failed to get genres from database"
        assert len(genres) > 0, "Empty list of genres"

    def test_get_one(self):
        genre = self.genre_service.get_one(1)

        assert genre is not None, "Failed to get genre from database"
        assert genre.id == 1, "Wrong genre id"
        assert genre.name == "Test name 1", "Wrong genre name"
