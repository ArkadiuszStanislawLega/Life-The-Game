from Models.location import Location
from Models.map_cell import MapCell
from Models.logbook import Logbook


class Map(Logbook):
    MAP_WIDTH = 10
    MAP_HEIGHT = 10

    def __init__(self):
        self.__cell_container = {}

        for x in range(self.MAP_WIDTH):
            for y in range(self.MAP_HEIGHT):
                location = Location()
                location.X = x
                location.Y = y

                map_cell = MapCell()
                map_cell.location = location

        self._add_log("Utworzono mapę.")
