from domainmodel.movie import Movie
from domainmodel.review import Review



class User:
    def __init__(self, user_name: str, password: str):
        if isinstance(user_name, str) and len(user_name.strip()) > 0:
            self.__user_name = user_name.strip()
            self.__user_name = user_name.lower()
        else:
            self.__user_name = None
        if isinstance(password, str):
            self.__password = password
        else:
            self.__password = None
        self.__watched_movies = []
        self.__reviews = []
        self.__time_spent_watching_movies_minutes = 0

    def __repr__(self):
        return f"<User {self.__user_name}>"

    def __eq__(self, other):
        if isinstance(other, User):
            return self.__user_name == other.user_name
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, User):
            return self.__user_name < other.user_name

    def __hash__(self):
        return hash((self.__user_name, self.__password))

    def watch_movie(self, movie: Movie):
        if isinstance(movie, Movie):
            if movie not in self.__watched_movies:
                self.__watched_movies.append(movie)
            self.__time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review: Review):
        if isinstance(review, Review):
            if review not in self.__reviews:
                self.__reviews.append(review)


    @property
    def user_name(self) -> str:
        return self.__user_name

    @property
    def password(self) -> str:
        return self.__password

    @property
    def watched_movies(self) -> list:
        return self.__watched_movies

    @property
    def reviews(self) -> list:
        return self.__reviews

    @property
    def time_spent_watching_movies_minutes(self) -> int:
        return int(self.__time_spent_watching_movies_minutes)

