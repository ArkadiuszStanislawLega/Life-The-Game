"""Klasa LifeCell"""

from Models.location import Location
from Models.basic_model import BasicModel


class LifeCell(BasicModel):
    """Klasa reprezentująca pojedynczą żywą komórkę.

    Arguments:
        BasicModel {BasicModel} -- Interfejs pozwalający na łatwe połączenie
                                    modelu z wiokiem i kontrolerami.
    """
    CHARACTER_REPRESENTING_AN_LIVE_CELL = 'O'
    CHARACTER_REPRESENTING_AN_DEAD_CELL = 'X'

    def __init__(self):
        """Jedna komórka życiowa, musi posiadać swoją lokację oraz ma dwa możliwe
            stany żywa lub martwa.
        """
        super().__init__()
        self.__is_alive = True
        self.__location = Location()
        self.__name = ""

    def __str__(self):
        if self.__is_alive:
            return self.CHARACTER_REPRESENTING_AN_LIVE_CELL
        return self.CHARACTER_REPRESENTING_AN_DEAD_CELL

    @property
    def name(self):
        """Udostępnia nazwę komórki.

        Returns:
            [str] -- nazwa komórki - przyjmuje wartość coordynatów lokacji.
        """
        return f'{self.__location}'

    @property
    def location(self):
        """Udostępnia aktualną lokalizację komórki.

        Returns:
            [Location] -- aktualna lokalizacja komórki.
        """
        return self.__location

    @property
    def is_alive(self):
        """Udostępnia flagę wskazującą czy komórka żyje.

        Returns:
            [bool] -- flaga wskazująca czy komórka żyje - jeśli True to żyje.
        """
        return self.__is_alive

    @is_alive.setter
    def is_alive(self, value):
        """Pozwala na zmianę flagi która wskazuje czy komórka żyje.

        Arguments:
            value {bool} -- jeśli wartość jest True to komórka żyje.
        """
        self.is_alive = value

    @location.setter
    def location(self, value):
        """Pozwala na zmianę lokalizacji komórki.

        Arguments:
            value {Location} -- nowa lokalizacja komórki.
        """
        self.__location = value

    def modify(self, *args, **kwargs):
        if len(args) > 0:
            self.__is_alive = args[0]
            self.notify()

    def notify(self):
        for view in self._obs_list.values():
            view.update(self)
