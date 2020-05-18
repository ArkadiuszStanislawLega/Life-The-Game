"""Autor: Arkadiusz Łęga, email:horemheb@vp.pl"""
from Library.colours import colours


class MapSettings:
    """Podstawowe ustawienia przewidziane dla widoku mapy."""

    def __init__(self, cell_width=10, cell_height=10):
        """Ustawia podstawowe wartości widoku mapy podane w
        argumentach.

        Keyword Arguments:
            cell_width {int} -- szerokość pojedynczej komórki podana
                                w pikselach (default: {10})
            cell_height {int} -- wysokość pojednycznej komórki podana
                                w pikselach (default: {10})
        """
        self.__cell_width = cell_width
        self.__cell_height = cell_height
        self.__cell_colour = colours.MATRIX

    @property
    def cell_width(self: int):
        """Szerokość komórki podana w pikselach.

        Returns:
            [int] -- szerokość komórki.
        """
        return self.__cell_width

    @property
    def cell_height(self):
        """Wysokość komórki podana w pikselach.

        Returns:
            [int] -- wysokość komórki.
        """
        return self.__cell_height

    @property
    def cell_colour(self):
        """Kolor komórki.

        Returns:
            [RGB] -- kolor komórki.
        """
        return self.__cell_colour

    @cell_colour.setter
    def cell_colour(self, value):
        """Pozwala na zmianę koloru komórki.

        Arguments:
            value {RGB} -- nowa wartość koloru komórki.
        """
        self.__cell_colour = value
