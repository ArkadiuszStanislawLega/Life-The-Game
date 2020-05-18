"""Autor: Arkadiusz Łęga, email:horemheb@vp.pl"""
from Library.colours import colours


class ViewSettings:
    """Podstawowe ustawienia potrzebne do wyświetlenia głównego okna aplikacji."""

    def __init__(self, model):
        """Ustawia wszystkie właściowści widoku aplikacji.

        Arguments:
            model {[Game]} -- instancja klasy sterująca aplikacją.
        """
        self.__model = model
        self.__window_title = "Life the game"
        self.__window_background = colours.BLACK
        self.__cell_width = 10
        self.__cell_height = 10

        self.__window_width = self.__model.map.width * self.__cell_width
        self.__window_height = self.__model.map.height * self.__cell_height

    @property
    def cell_width(self):
        """Szerokość każdej komórki.

        Returns:
            [int] -- szerokość każdej komórki.
        """
        return self.__cell_width

    @cell_width.setter
    def cell_width(self, value: int):
        self.__cell_width = value

    @property
    def cell_height(self):
        """Wysokość każdej komórki.

        Returns:
            [int] -- wysokość każdej komórki.
        """
        return self.__cell_height

    @cell_height.setter
    def cell_height(self, value: int):
        self.__cell_height = value

    @property
    def cell_colour(self):
        """Kolor każdej żywej komórki.

        Returns:
            [RGB] -- kolor żywej komórki.
        """
        return self.__cell_colour

    @cell_colour.setter
    def cell_colour(self, value: (int, int, int)):
        self.__cell_colour = value

    @property
    def window_title(self):
        """Tytuł okna aplikacji.

        Returns:
            [str] -- tytuł okna aplikacji.
        """
        return self.__window_title

    @window_title.setter
    def window_title(self, value: str):
        self.__window_title = value

    @property
    def window_background(self):
        """Kolor tła okna aplikacji.

        Returns:
            [RGB] -- kolor tła okna apliakcji.
        """
        return self.__window_background

    @window_background.setter
    def window_background(self, value: (int, int, int)):
        self.__window_background = value

    @property
    def window_width(self):
        """Szerokość okna aplikacji.

        Returns:
            [int] -- Szerokość okna aplikacji.
        """
        return self.__window_width

    @property
    def window_height(self):
        """Wysokość okna aplikacji.

        Returns:
            [int] -- wysokość okna aplikacji.
        """
        return self.__window_height

    @property
    def window_size(self):
        """Wymiary okna aplikacji.

        Returns:
            [(int,int)] -- wymiary okna aplikacji.
        """
        return (self.__window_width, self.__window_height)
