from app.dao.models.genre_model import Genre


# ----------------------------------------------------------------------------------------------------------------------
# Create DAO model
class GenreDAO:
    """
    DAO for genres
    """
    def __init__(self, session):
        """
        Initialize DAO with session \n
        :param session: Database session
        """
        self.session = session

    def get_all(self) -> list[Genre] | list:
        """
        Get all genres from database \n
        :return: List of genre instances
        """
        return self.session.query(Genre).all()

    def get_one(self, genre_id: int) -> Genre:
        """
        Get one genre from database by id \n
        :param genre_id: ID of genre
        :return: Genre instance
        """
        return self.session.query(Genre).get(genre_id)
