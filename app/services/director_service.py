# ----------------------------------------------------------------------------------------------------------------------
# Create Service for DirectorDAO object
class DirectorService:
    """
    Service for DirectorDAO
    """
    def __init__(self, dao):
        """
        Initialize Service with DAO object
        :param dao: DirectorDAO object
        """
        self.dao = dao

    def get_all(self) -> list:
        """
        Get all directors from database

        :return: List of director instances
        """
        return self.dao.get_all()

    def get_one(self, director_id: int) -> object:
        """
        Get one director from database by id

        :param director_id: ID of director
        :return: Director instance
        """
        return self.dao.get_one(director_id)
