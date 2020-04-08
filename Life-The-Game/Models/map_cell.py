from Models.location import Location
from Models.life_cell import LifeCell


class MapCell:
    """
    Model przedstawiający jedno pole mapy.

    Returns:
        [MapCell] -- Jedno pole mapy.
    """

    def __init__(self):
        self.__life_cell = None
        self.__is_occupied = False
        self.__location = Location()

    @property
    def is_occupied(self):
        return self.__is_occupied

    @property
    def life_cell(self):
        return self.__life_cell

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value: Location):
        self.__location = value

    def is_put_life_in_cell(self, life_cell: LifeCell):
        """
        Wstawia komórkę życiową do pola mapy jeżeli jest ona pusta i podana w argumencie komórka jest komórką życiową.

        Arguments:
            life_cell {LifeCell} -- komórka życiowa która ma zostać wstawiona.

        Returns:
            [boolean] -- prawda jeżeli udało się wstawić komórkę życiową.
        """
        if self.__life_cell is None and isinstance(LifeCell, life_cell):
            self.__life_cell = life_cell
            self.__is_occupied = True
            return True
        return False

    def clear_cell(self):
        """
        Czyści pole mapy z komórki życiowej jeżeli taka jest na polu.
        """
        if self.__life_cell is not None:
            self.__life_cell = None
            self.__is_occupied = False

    def __str__(self):
        if self.__is_occupied:
            return self.__life_cell
        else:
            return '_'
