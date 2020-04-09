from Models.location import Location


class LifeCell:
    def __init__(self):
        self.__is_alive = False
        self.__location = Location()

    def __str__(self):
        if self.__is_alive:
            return "O"
        return "X"

    @property
    def location(self):
        return self.__location

    @property
    def is_alive(self):
        return self.__is_alive

    @is_alive.setter
    def is_alive(self, value: bool):
        self.__is_alive = value

    @location.setter
    def location(self, value):
        self.__location = value
