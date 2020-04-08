from Models.location import Location
from Models.map_cell import MapCell
from Models.logbook import Logbook


class Map(Logbook):
    MAP_WIDTH = 20
    MAP_HEIGHT = 10

    def __init__(self):
        self.__cell_container = {str: MapCell}

        for y in range(self.MAP_HEIGHT):
            for x in range(self.MAP_WIDTH):
                location = Location()
                location.X = x
                location.Y = y

                map_cell = MapCell()
                map_cell.location = location

                self.__cell_container[f'{location}'] = map_cell

        self._add_log("Utworzono mapę.")

    @property
    def container(self):
        return self.__cell_container

    def print_map(self):
        for y in range(self.MAP_HEIGHT):
            for x in range(self.MAP_WIDTH):
                location = Location()
                location.X = x
                location.Y = y
                coordinates = f'{location}'
                print(f'{self.__cell_container[coordinates]} ', end="")
                if x == self.MAP_WIDTH - 1:
                    print("\n")
