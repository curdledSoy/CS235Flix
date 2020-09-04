from domainmodel.user import User
from domainmodel.watchlist import WatchList


class UserGroup:
    def __init__(self, owner: User, name = None):
        if name is None or len(name.strip()) == 0 or not isinstance(name, str):
            self.__group_name = "New Group"
        else:
            self.__group_name = name.strip()
        self.__owner = owner
        self.__members = [owner]
        self.__watchlist = WatchList()

    def __repr__(self) -> str:
        return f"<UserGroup {self.__group_name}>"

    def __eq__(self, other):
        if isinstance(other, UserGroup):
            return (self.__owner,self.__members) == (other.__owner, other.__members)

    def __hash__(self):
        return hash((self.__group_name,self.__owner,self.__members))

    @property
    def group_name(self) -> str:
        return self.__group_name

    @group_name.setter
    def group_name(self, new_name):
        if new_name and len(new_name.strip()) > 0 and isinstance(new_name, str):
            self.__group_name = new_name.strip()

    @property
    def owner(self) -> User:
        return self.__owner

    @property
    def watchlist(self):
        return self.__watchlist

    @property
    def members(self):
        return self.__members

    def watch_movie(self, movie):
        for user in self.__members:
            user.watch_movie(movie)

    def add_member(self, user: User):
        if isinstance(user, User) and user not in self.__members:
            if self.__owner != user:
                self.__members.append(user)

    def remove_member(self, user: User):
        if isinstance(user, User) and user in self.__members:
            if self.__owner != user:
                self.__members.remove(user)





