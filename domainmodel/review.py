from datetime import datetime

from domainmodel.movie import Movie


class Review:
    def __init__(self, movie: Movie, review_text: str, rating: int):
        if isinstance(movie, Movie):
            self.__movie = movie
        else:
            self.__movie = None
        if isinstance(review_text, str) and len(review_text.strip()) > 0:
            self.__review_text = review_text.strip()
        else:
            self.__review_text = None
        if isinstance(rating, int) and 10 >= rating >= 1:
            self.__rating = rating
        else:
            self.__rating = None

        self.__timestamp = datetime.today()

    def __eq__(self, other):
        if isinstance(other, Review):
            return (self.__movie, self.__review_text, self.__rating, self.__timestamp) == (
            other.movie, other.review_text, other.rating, other.timestamp)
        else:
            return False

    def __repr__(self):
        return f"<Review {self.__movie}, {self.__review_text}, {self.__rating}, {self.__timestamp}>"

    @property
    def movie(self):
        return self.__movie

    @property
    def review_text(self):
        return self.__review_text

    @property
    def rating(self):
        return self.__rating

    @property
    def timestamp(self):
        return self.__timestamp