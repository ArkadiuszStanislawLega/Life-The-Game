from Models.location import Location
from Models.map_cell import MapCell
from Models.basic_model import BasicModel


class Map(BasicModel):
    def __init__(self, width, height):
        super().__init__()
        self.__cells_container = {}
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
        return self.__cells_container

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

                self.__cells_container[f'{location}'] = map_cell

    def modify(self, *args, **kwargs):
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "is_was_occupied":
                    self.__is_was_occupied = value
                    self.notify(grade=self.__is_was_occupied)

            key = kwargs.get("key")
            value = kwargs.get("value")

            if key and value:
                self.__cells_container.get(key).is_put_life_in_cell(value)
                new_key = f"MapCellView:{value.location}"
                self.notify(name=new_key)
                return True

    def notify(self, *args, **kwargs):
        if len(kwargs) > 0:
            self._obs_list.get("MapView").update(**kwargs)
