from domainmodel.movie import Movie
import random


class WatchList:
    def __init__(self):
        self.__watchlist = []
        self.__movie_index = 0


    def add_movie(self, movie: Movie):
        if isinstance(movie, Movie) and movie not in self.__watchlist:
            self.__watchlist.append(movie)

    def remove_movie(self, movie: Movie):
        if isinstance(movie, Movie) and movie in self.__watchlist:
            self.__watchlist.remove(movie)

    def select_movie_to_watch(self, index: int):
        if isinstance(index, int) and index in range(len(self.__watchlist)):
            return self.__watchlist[index]
        else:
            return None

    def shuffle_select_movie_to_watch(self):
        return self.__watchlist[random.randint(0, len(self.__watchlist))]

    def size(self):
        return len(self.__watchlist)

    def first_movie_in_watchlist(self):
        if self.size() != 0:
            return self.__watchlist[0]
        else:
            return None

    def __iter__(self):
        return self

    def __next__(self):
        if self.__movie_index < len(self.__watchlist):
            next_movie = self.__watchlist[self.__movie_index]
            self.__movie_index += 1
            return next_movie
        else:
            raise StopIteration



