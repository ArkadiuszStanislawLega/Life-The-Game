from Models.location import Location


class LifeCell:
    def __init__(self):
        self.__is_alive = False
        self.__location = ''

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        self.__location = value

    def __str__(self):
        if self.__is_alive:
            return f'O'
        else:
            return f'X'
