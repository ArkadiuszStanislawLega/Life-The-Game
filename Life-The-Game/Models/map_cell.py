from Models.location import Location
from Models.life_cell import LifeCell


class MapCell:
    def __init__(self):
        self.__is_occupied = False
        self.__location = Location()

    @property
    def is_occupied(self):
        return self.__is_occupied

    @property
    def location(self):
        return self.__location
