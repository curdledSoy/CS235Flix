from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director


class Movie:
    def __init__(self, title: str, release_year: int):
        if isinstance(title, str):
            title = title.strip()
            if len(title) > 0:
                self.__title = title
        else:
            self.__title = None
        if release_year >= 1900 and isinstance(release_year, int):
            self.__release_year = release_year
        else:
            self.__release_year = None
        self.__description = ""
        self.__director = None
        self.__actors = []
        self.__genres = []
        self.__runtime_minutes = 0
        self.__rank = None
        self.__rating = None
        self.__votes = None
        self.__revenue_in_millions = None
        self.__metascore = None

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str):
            new_title = new_title.strip()
            if len(new_title) > 0:
                self.__title = new_title

    @property
    def release_year(self) -> int:
        return self.__release_year

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, new_description):
        if isinstance(new_description, str) and len(new_description.strip()) > 0:
            self.__description = new_description.strip()

    @property
    def director(self) -> Director:
        return self.__director

    @director.setter
    def director(self, new_director):
        if isinstance(new_director, Director):
            self.__director = new_director

    @property
    def actors(self) -> list:
        for i in range(len(self.__actors)):
            actor1 = self.__actors[i]
            for actor2 in self.__actors[:i] + self.__actors[i + 1:]:
                actor1.add_actor_colleague(actor2)
        self.__actors.sort()
        return self.__actors

    @actors.setter
    def actors(self, new_actors):
        if isinstance(new_actors, list):
            self.__actors = new_actors

    @property
    def genres(self) -> list:
        self.__genres.sort()
        return self.__genres

    @genres.setter
    def genres(self, new_genres):
        if isinstance(new_genres, list):
            self.__genres = new_genres

    @property
    def runtime_minutes(self) -> int:
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, new_runtime: int):
        if new_runtime > 0 & isinstance(new_runtime, int):
            self.__runtime_minutes = new_runtime
        else:
            raise ValueError()

    @property
    def rank(self) -> int:
        return self.__rank

    @rank.setter
    def rank(self, new_ranking: int):
        if isinstance(new_ranking, int) and new_ranking > 0:
            self.__rank = new_ranking

    @property
    def rating(self) -> int:
        return self.__rating

    @rating.setter
    def rating(self, new_rating: int):
        if isinstance(new_rating, int) and 10 >= new_rating >= 0:
            self.__rating = new_rating

    @property
    def votes(self):
        return self.__votes

    @votes.setter
    def votes(self, new_votes: int):
        if isinstance(new_votes, int) and new_votes >= 0:
            self.__votes = new_votes

    @property
    def revenue(self):
        return self.__revenue_in_millions

    @revenue.setter
    def revenue(self, new_revenue: float):
        if isinstance(new_revenue, float):
            if new_revenue > 0.0:
                self.__revenue_in_millions = new_revenue

    @property
    def metascore(self):
        return self.__metascore

    @metascore.setter
    def metascore(self, new_metascore: int):
        if isinstance(new_metascore, int) and 0 >= new_metascore <= 100:
            self.__metascore = new_metascore

    def __repr__(self):
        return f"<Movie {self.__title}, {self.__release_year}>"

    def __eq__(self, other):
        return (self.__title, self.__release_year) == (other.title, other.release_year)

    def __lt__(self, other):
        return (self.__title, self.__release_year) < (other.title, other.release_year)

    def __hash__(self):
        return hash(self.__title + " " + str(self.__release_year))

    def add_actor(self, actor):
        if isinstance(actor, Actor):
            if actor not in self.__actors:
                self.__actors.append(actor)

    def remove_actor(self, actor):
        if actor in self.__actors:
            self.__actors.remove(actor)

    def add_genre(self, genre):
        if isinstance(genre, Genre):
            if genre not in self.__genres:
                self.__genres.append(genre)

    def remove_genre(self, genre):
        if genre in self.__genres:
            self.__genres.remove(genre)
