import csv

from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director


class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__actors = set()
        self.__directors = set()
        self.__genres = set()
        self.__movies = []

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            for row in movie_file_reader:
                try:
                    rank = int(row['Rank'])
                except ValueError:
                    rank = None
                title = row['Title']
                genres = row['Genre'].split(',')
                description = row['Description']
                actors = row['Actors'].split(',')
                try:
                    release_year = int(row['Year'])
                except ValueError:
                    release_year = None
                try:
                    run_time = int(row['Runtime (Minutes)'])
                except ValueError:
                    run_time = None
                try:
                    rating = int(row['Rating'])
                except ValueError:
                    rating = 0
                try:
                    votes = int(row['Votes'])
                except ValueError:
                    votes = 0
                director = Director(row['Director'])
                try:
                    revenue = float(row['Revenue (Millions)'])
                except ValueError:
                    revenue = None
                try:
                    metascore = int(row['Metascore'])
                except ValueError:
                    metascore = None

                mov = Movie(title, release_year)
                mov.director = director
                mov.description = description
                mov.metascore = metascore
                mov.rank = rank
                mov.runtime_minutes = run_time
                mov.rating = rating
                mov.votes = votes
                mov.revenue = revenue

                self.load_actors(mov, actors)

                if director not in self.__directors:
                    self.__directors.add(director)

                self.load_genres(mov, genres)

                if mov not in self.__movies:
                    self.__movies.append(mov)

    def load_actors(self, movie, actors):
        for name in actors:
            temp_actor = Actor(name)
            movie.add_actor(temp_actor)
            if temp_actor not in self.__actors:
                self.__actors.add(temp_actor)

    def load_genres(self, movie, genres):
        for genre in genres:
            temp_genre = Genre(genre)
            if temp_genre not in self.__genres:
                self.__genres.add(temp_genre)
            movie.add_genre(temp_genre)

    @property
    def dataset_of_movies(self):
        return self.__movies

    @property
    def dataset_of_actors(self):
        return self.__actors

    @property
    def dataset_of_directors(self):
        return self.__directors

    @property
    def dataset_of_genres(self):
        return self.__genres
