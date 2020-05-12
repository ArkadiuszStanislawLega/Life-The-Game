from Models.location import Location
from Models.life_cell import LifeCell
from Models.basic_model import BasicModel


class MapCell(BasicModel):
    """
    Model przedstawiający jedno pole mapy.

    Returns:
        [MapCell] -- Jedno pole mapy.
    """

    CHARACTER_REPRESENTING_AN_EMPTY_MAP_FIELD = ' '

    def __init__(self):
        super().__init__()
        self.__life_cell = None
        self.__is_occupied = False
        self.__is_was_occupied = False
        self.__location = Location()

    @property
    def is_was_occupied(self):
        return self.__is_was_occupied

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
        if self.__life_cell is None and isinstance(life_cell, LifeCell):
            self.__life_cell = life_cell
            self.__is_occupied = True
            self.modify(is_was_occupied=True)
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
            return f'{self.__life_cell}'
        else:
            return self.CHARACTER_REPRESENTING_AN_EMPTY_MAP_FIELD

    def modify(self, *args, **kwargs):
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "is_was_occupied" and self.__is_was_occupied == False:
                    self.__is_was_occupied = value
                    self.notify(is_was_occupied=self.__is_was_occupied)

    def notify(self, *args, **kwargs):
        if len(kwargs) > 0:
            self._obs_list.get(f'MapCellView:{self.__location}').update(kwargs)
