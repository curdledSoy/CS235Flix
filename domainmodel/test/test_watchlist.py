import pytest
from domainmodel.watchlist import WatchList
from domainmodel.movie import Movie

class TestWatchlistMethods:
    @pytest.fixture
    def watchlist(self):
        return WatchList()

    def test_construction(self, watchlist):
        assert watchlist.first_movie_in_watchlist() == None
        assert watchlist.size() == 0

    def test_iter(self, watchlist):
        assert iter(watchlist)

    def test_next(self, watchlist):
        movie = Movie("Moana", 2016)
        watchlist.add_movie(movie)
        assert next(watchlist) == movie
        with pytest.raises(StopIteration):
            next(watchlist)

    def test_add_movie(self, watchlist):
        movie = Movie("Moana", 2016)
        watchlist.add_movie(movie)
        assert watchlist.first_movie_in_watchlist() == movie

    def test_remove_movie(self,watchlist):
        movie1 = Movie("The 100", 2016)
        movie2 = Movie("Bones", 2004)
        watchlist.add_movie(movie1)
        watchlist.add_movie(movie2)
        watchlist.remove_movie(movie2)
        assert watchlist.size() == 1

    def test_select_movie_to_watch(self, watchlist):
        assert watchlist.select_movie_to_watch(1) == None
        assert watchlist.select_movie_to_watch('a') == None
        movie1 = Movie("The 100", 2016)
        movie2 = Movie("Bones", 2004)
        watchlist.add_movie(movie1)
        watchlist.add_movie(movie2)
        assert watchlist.select_movie_to_watch(1) == movie2

    def test_size(self, watchlist):
        movie1 = Movie("The 100", 2016)
        movie2 = Movie("Bones", 2004)
        watchlist.add_movie(movie1)
        watchlist.add_movie(movie2)
        assert watchlist.size() == 2

