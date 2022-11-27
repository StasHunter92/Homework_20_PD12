from app.dao.models.movie_model import Movie


# ----------------------------------------------------------------------------------------------------------------------
# Create DAO model
class MovieDAO:
    """
    DAO for movies
    """
    def __init__(self, session):
        """
        Initialize DAO with session \n
        :param session: Database session
        """
        self.session = session

    def get_all(self, data: dict) -> list[Movie] | list:
        """
        Get all movies from database \n
        :param data: Filters for search movies
        :return: List of movie instances
        """
        movies_query = self.session.query(Movie)

        if data.get('director_id') is not None:
            movies_query = movies_query.filter(Movie.director_id == data.get('director_id'))
        if data.get('genre_id') is not None:
            movies_query = movies_query.filter(Movie.genre_id == data.get('genre_id'))
        if data.get('year') is not None:
            movies_query = movies_query.filter(Movie.year == data.get('year'))

        return movies_query.all()

    def get_one(self, movie_id: int) -> Movie:
        """
        Get one movie from database by id \n
        :param movie_id: ID of movie
        :return: Movie instance
        """
        return self.session.query(Movie).get(movie_id)

    def create(self, data: dict) -> str:
        """
        Create a new movie \n
        :param data: Dictionary with new information
        :return: Location of new movie
        """
        new_movie: Movie = Movie(**data)

        self.session.add(new_movie)

        self.session.flush()
        location: str = f'/movies/{new_movie.id}'

        self.session.commit()
        return location

    def update(self, movie: Movie) -> None:
        """
        Update movie information \n
        :param movie: Movie instance
        :return: Movie instance
        """
        self.session.add(movie)
        self.session.commit()

    def delete(self, movie: Movie) -> None:
        """
        Delete movie from database \n
        :param movie: Movie instance
        :return: Nothing
        """
        self.session.delete(movie)
        self.session.commit()
