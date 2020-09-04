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
                rank = int(row['Rank'])
                title = row['Title']
                genres = row['Genre'].split(',')
                description = row['Description']
                actors = row['Actors'].split(',')
                release_year = int(row['Year'])
                run_time = int(row['Runtime (Minutes)'])
                rating = float(row['Rating'])
                votes = int(row['Votes'])
                director = Director(row['Director'])
                try:
                    revenue = float(row['Revenue (Millions)'])
                except:
                    revenue = None
                try:
                    metascore = int(row['Metascore'])
                except:
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

                for name in actors:
                    temp_actor = Actor(name)
                    mov.add_actor(temp_actor)
                    if temp_actor not in self.__actors:
                        self.__actors.add(temp_actor)

                if mov.director not in self.__directors:
                    self.__directors.add(director)

                for genre in genres:
                    temp_genre = Genre(genre)
                    if temp_genre not in self.__genres:
                        self.__genres.add(temp_genre)
                    mov.add_genre(temp_genre)

                if mov not in self.__movies:
                    self.__movies.append(mov)

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
