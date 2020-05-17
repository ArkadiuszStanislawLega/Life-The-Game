"""Klasa MapCell"""

from Models.location import Location
from Models.life_cell import LifeCell
from Models.basic_model import BasicModel


class MapCell(BasicModel):
    """
    Model przedstawiający jedno pole mapy.
    W którym może być przechowywana jedna komórka życiowa.
    Komóra mapy zapamiętuje czy było na niej życie.
    Każda komórka ma swoje określone koordynaty.

    Returns:
        [MapCell] -- Jedno pole mapy.
    """

    def __init__(self):
        """Generuje podstawowe wartości komórki."""
        super().__init__()
        self.__life_cell = None
        self.__is_occupied = False
        self.__is_was_occupied = False
        self.__location = Location()

    @property
    def is_was_occupied(self):
        """Umożliwia dostęp do falgi wskauzjącej czy na komórce była
        kiedyś komórka życia.

        Returns:
            [bool] -- flaga wskazująca czy było na komórce życie
        """
        return self.__is_was_occupied

    @property
    def is_occupied(self):
        """Umożliwia dostęp do falgi wskazującej czy na komórce aktualnie
        jest komórka życia.

        Returns:
            [bool] -- flaga wskazująca czy jest na niej komórka życia
        """
        return self.__is_occupied

    @property
    def life_cell(self):
        """Umożliwia dostęp do atkulnie przebywającej na komórce, komórki życia.

        Returns:
            [LifeCell] -- znajdująca się na mapie komórka życia.
        """
        return self.__life_cell

    @property
    def location(self):
        """Umożliwia dostęp do koordynatów komórki.

        Returns:
            [Location] -- koordynaty komórki.
        """
        return self.__location

    @location.setter
    def location(self, value: Location):
        """Umożliwia zmianę koordynatów komórki.

        Arguments:
            value {Location} -- nowe koordynaty komórki.
        """
        self.__location = value

    def is_put_life_in_cell(self, life_cell: LifeCell):
        """
        Wstawia komórkę życiową do pola mapy jeżeli jest ona pusta i podana w
        argumencie komórka jest komórką życiową.

        Arguments:
            life_cell {LifeCell} -- komórka życiowa która ma zostać wstawiona.

        Returns:
            [boolean] -- prawda jeżeli udało się wstawić komórkę życiową.
        """
        if self.__life_cell is None and isinstance(life_cell, LifeCell):
            self.__life_cell = life_cell
            self.__is_was_occupied = True
            self.__is_occupied = True

            return True
        return False

    def clear_cell(self):
        """ Czyści pole mapy z komórki życiowej jeżeli taka jest na polu."""
        if self.__life_cell is not None or isinstance(self.__life_cell, LifeCell):
            if not self.__life_cell.is_alive:
                self.__life_cell = None
                self.__is_occupied = False
                self.notify()

    def __str__(self):
        if self.__is_occupied:
            return f'{self.__life_cell}'

        return f'EmptyMapCell:{self.__location}'

    def modify(self, *args, **kwargs):
        pass

    def notify(self):
        for view in self._obs_list.values():
            view.update(self)
