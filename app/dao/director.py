from app.dao.models.director_model import Director


# ----------------------------------------------------------------------------------------------------------------------
# Create DAO model
class DirectorDAO:
    """
    DAO for directors
    """
    def __init__(self, session):
        """
        Initialize DAO with session

        :param session: Database session
        """
        self.session = session

    def get_all(self) -> list[Director] | list:
        """
        Get all directors from database

        :return: List of director instances
        """
        return self.session.query(Director).all()

    def get_one(self, director_id: int) -> Director:
        """
        Get one director from database by id

        :param director_id: ID of director
        :return: Director instance
        """
        return self.session.query(Director).get(director_id)
