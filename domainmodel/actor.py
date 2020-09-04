
class Actor:
    def __init__(self, full_name):
        if full_name == "" or type(full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = full_name.strip()
        self.__has_worked_with = []

    @property
    def actor_full_name(self):
        return self.__actor_full_name

    def __repr__(self) -> str:
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other) -> bool:
        return self.__actor_full_name == other.actor_full_name

    def __lt__(self, other):
        return self.__actor_full_name < other.actor_full_name

    def __hash__(self) -> int:
        return hash(self.__actor_full_name)

    def add_actor_colleague(self, colleague):
        if colleague not in self.__has_worked_with:
            self.__has_worked_with.append(colleague)
            colleague.add_actor_colleague(self)

    def check_if_this_actor_worked_with(self, colleague):
        return colleague in self.__has_worked_with
