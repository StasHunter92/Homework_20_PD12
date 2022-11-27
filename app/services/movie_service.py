# ----------------------------------------------------------------------------------------------------------------------
# Create Service for MovieDAO object
class MovieService:
    """
    Service for MovieDAO
    """
    def __init__(self, dao):
        """
        Initialize Service with DAO object \n
        :param dao: MovieDAO object
        """
        self.dao = dao

    def get_all(self, data: dict) -> list:
        """
        Get all movies from database \n
        :param data: Filters for search movies
        :return: List of movie instances
        """
        return self.dao.get_all(data)

    def get_one(self, movie_id: int) -> object:
        """
        Get one movie from database by id \n
        :param movie_id: ID of movie
        :return: Movie instance
        """
        return self.dao.get_one(movie_id)

    def create(self, data: dict) -> str:
        """
        Create a new movie \n
        :param data: Dictionary with new information
        :return: Location of new movie
        """
        return self.dao.create(data)

    def update(self, data: dict) -> None:
        """
        Update movie information \n
        :param data: Dictionary with update information
        :return: Movie instance
        """
        movie_id = data.get('id')
        movie = self.dao.get_one(movie_id)

        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.year = data.get("year")
        movie.rating = data.get("rating")
        movie.genre_id = data.get("genre_id")
        movie.director_id = data.get("director_id")

        self.dao.update(movie)

    def delete(self, movie_id: int) -> None:
        """
        Delete movie from database \n
        :param movie_id: ID of movie
        :return: Nothing
        """
        movie = self.dao.get_one(movie_id)
        self.dao.delete(movie)
