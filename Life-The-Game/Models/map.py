from Models.location import Location
from Models.map_cell import MapCell


class Map:
    def __init__(self, width, height):
        self.__cell_container = {str: MapCell}
        self.__width = width
        self.__height = height

        self.__create_empty_cells()

    @property
    def container(self):
        """
        Kontener z komórkami mapy.

        Returns:
            [dictionary{str:MapCell}] -- Słownik z komórkami mapy, kluczami są koordynaty lokacji (x, y)
        """
        return self.__cell_container

    @property
    def width(self):
        """
        Szerokość mapy.

        Returns:
            [int] -- Podana w argumencie szerokość mapy.
        """
        return self.__width

    @property
    def height(self):
        """
        Wysokość mapy.

        Returns:
            [int] -- Podana w argumencie wysokość mapy.
        """
        return self.__height

    def __create_empty_cells(self):
        """
        Tworzy wszystkie komórki potrzebne do działania gry.
        """
        for y in range(self.__height):
            for x in range(self.__width):
                location = Location()
                location.X = x
                location.Y = y

                map_cell = MapCell()
                map_cell.location = location

                self.__cell_container[f'{location}'] = map_cell

    def print_map(self):
        """
        Rysuje mapę w konsoli.
        """
        for y in range(self.__height):
            for x in range(self.__width):
                location = Location()
                location.X = x
                location.Y = y
                coordinates = f'{location}'
                print(f'{self.__cell_container[coordinates]}', end="")
                if x == self.__width - 1:
                    print()
