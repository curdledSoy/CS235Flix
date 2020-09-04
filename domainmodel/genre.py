
class Genre:
    def __init__(self, genreName):
        if genreName == "" or type(genreName) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = genreName

    @property
    def genre_name(self) -> str:
        return self.__genre_name

    def __repr__(self):
        return f"<Genre {self.__genre_name}>"

    def __eq__(self, other):
        if isinstance(other,Genre):
            return self.__genre_name == other.genre_name
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Genre):
            return self.__genre_name < other.genre_name
        else:
            return False

    def __hash__(self):
        return hash(self.__genre_name)
