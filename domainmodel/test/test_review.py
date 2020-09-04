
import pytest
from domainmodel.review import Review
from domainmodel.movie import Movie
from datetime import datetime


class TestReviewMethods:
    @pytest.fixture
    def review(self):
        return Review(Movie('Moana', 2016), 'This Movie was really good', 10)

    def test_construction(self, review):
        assert review.movie == Movie('Moana', 2016)
        assert review.review_text == 'This Movie was really good'

    def test_eq(self, review):
        assert review != Review(Movie('Moana', 2016), 'This Movie was really good', 10)

    def test_movie(self, review):
        assert review.movie == Movie('Moana', 2016)
        assert Review('a', 'good movie', 8).movie is None

    def test_review_text(self, review):
        assert review.review_text == 'This Movie was really good'
        assert Review(Movie('Moana', 2016),10, 9).review_text is None

    def test_rating(self, review):
        assert review.rating == 10
        assert Review(Movie('Moana', 2016),'This Movie was really good', 'a').rating is None

    def test_timestamp(self, review):
        assert review.timestamp.date() == datetime.today().date()

