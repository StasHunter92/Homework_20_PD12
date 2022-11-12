# ----------------------------------------------------------------------------------------------------------------------
# Create Service for GenreDAO object
class GenreService:
    """
    Service for GenreDAO
    """
    def __init__(self, dao):
        """
        Initialize Service with DAO object
        :param dao: GenreDAO object
        """
        self.dao = dao

    def get_all(self) -> list:
        """
        Get all genres from database

        :return: List of genre instances
        """
        return self.dao.get_all()

    def get_one(self, genre_id: int) -> object:
        """
        Get one genre from database by id

        :param genre_id: ID of genre
        :return: Genre instance
        """
        return self.dao.get_one(genre_id)
