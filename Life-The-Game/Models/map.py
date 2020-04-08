from Models.location import Location
from Models.map_cell import MapCell


class Map:
    MAP_WIDTH = 10
    MAP_HEIGHT = 10

    def __init__(self):
        self.__cell_container = {}
