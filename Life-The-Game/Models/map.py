from Models.location import Location
from Models.map_cell import MapCell
from Models.logbook import Logbook


class Map(Logbook):
    def __init__(self, width, height):
        self.__cell_container = {str: MapCell}
        self.__width = width
        self.__height = height

        for y in range(self.__height):
            for x in range(self.__width):
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

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def print_map(self):
        for y in range(self.__height):
            for x in range(self.__width):
                location = Location()
                location.X = x
                location.Y = y
                coordinates = f'{location}'
                print(f'{self.__cell_container[coordinates]}', end="")
                if x == self.__width - 1:
                    print()
