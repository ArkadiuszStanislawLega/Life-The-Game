"""Klasa Map"""

from Models.location import Location
from Models.map_cell import MapCell
from Models.basic_model import BasicModel


class Map(BasicModel):
    """Klasa map, składa się komórek mapy które mają swoje koordynaty.
    Koordynaty rosną od lewego górnego rogu w prawo i w dół.
    Pierwszy koordynat ma wartość x, a drugi y.
    Górny prawy róg ma koordynaty (0, 0).
    Mapa jest generowana w zależności od podanych argumentów width, height.
    W zależności od nich tworzy tyle komórek mapy.

    Arguments:
        BasicModel {BasicModel} -- Klasa umożliwijąca w łatwy sposób połączenie
                                   modelu z widokiem oraz kontrolerów
    """

    def __init__(self, width, height):
        """Generuje wszystkie komórki mapy.
        W zależności od podanych wartości wysokości i szerokości.

        Arguments:
            width {int} -- szerokość mapy.
            height {int} -- wysokość mapy.
        """
        super().__init__()
        self.__map_cells_container = {}
        self.__life_cells = {}
        self.__width = width
        self.__height = height

        self.__create_empty_cells()

    @property
    def life_cells(self):
        """List z wszystkimi żywymi komórkami"""
        return self.__life_cells

    @property
    def map_cells_container(self):
        """
        Kontener z komórkami mapy.

        Returns:
            [dictionary{str:MapCell}] -- Słownik z komórkami mapy, kluczami są
                                            koordynaty lokacji (x, y)
        """
        return self.__map_cells_container

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
        for coordinate_y in range(self.__height):
            for coordinate_x in range(self.__width):
                location = Location()
                location.X = coordinate_x
                location.Y = coordinate_y

                map_cell = MapCell()
                map_cell.location = location

                self.__map_cells_container[f'{location}'] = map_cell

    def add_life_cell(self, life_cell):
        """ Dodaje nowo stworzoną życiową komórkę"""
        if not self.__life_cells.get(f'{life_cell.location}'):
            map_cell = self.__map_cells_container.get(f'{life_cell.location}')
            if map_cell.is_put_life_in_cell(life_cell):
                self.__life_cells[f'{life_cell.location}'] = life_cell
                return True

        return False

    def modify(self, *args, **kwargs):
        if len(args) > 0:
            if isinstance(args[0], MapCell):
                key = f"MapCellView:{args[0].location}"
                if not self.__map_cells_container.get(key):
                    self.__map_cells_container[key] = args[0]
                    self.__map_cells_container.get(
                        key).is_put_life_in_cell(args[0])
                    return True
                else:
                    self.__map_cells_container.update({key: args[0]})

        return False

    def notify(self):
        pass
