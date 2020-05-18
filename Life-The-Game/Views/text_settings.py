"""Autor: Arkadiusz Łęga, email:horemheb@vp.pl"""
import pygame
from Library.colours import colours


class TextSettings:
    """Podstawowe ustawienia tekstów wyświetlanych w  czasie rozgrywki."""

    def __init__(self):
        self.__row_height = 15
        self.__font_name = 'freesansbold.ttf'
        self.__font_colour = colours.WHITE
        self.__font_size = 12
        self.__left_margin = 15
        self.__background_colour = colours.BLACK
        self.__coordinate_x = self.__left_margin + 0
        self.__coordinate_y = 0
        self.__coordinates = (self.__coordinate_x, self.__coordinate_y)
        self.__font = pygame.font.Font(self.__font_name, self.__font_size)

    @property
    def row_height(self):
        """Wysokość jednego wiersza podana w pikselach.

        Returns:
            [int] -- szerokość jednego wiersza.
        """
        return self.__row_height

    @property
    def font_name(self):
        """Nazwa czcionki jaka jest używana do drukowania napisów.

        Returns:
            [str] -- nazwa czcionki używana do drukowania napisów.
        """
        return self.__font_name

    @font_name.setter
    def font_name(self, value: str):
        self.__font_name = value

    @property
    def font_colour(self):
        """Kolor czcionki.

        Returns:
            [RGB] -- kolor czcionki
        """
        return self.__font_colour

    @font_colour.setter
    def font_colour(self, value: (int, int, int)):
        self.__font_colour = value

    @property
    def font_size(self):
        """Wysokość czcionki.

        Returns:
            [int] -- Wysokość czcionki.
        """
        return self.__font_size

    @font_size.setter
    def font_size(self, value: int):
        self.__font_size = value

    @property
    def left_magin(self):
        """Wcięcie od krawędzi lewej ekranu strony przed drukowanie
        każdego napisu. Liczona w pikselach.

        Returns:
            [int] -- wcięcie od lewej strony ekranu.
        """
        return self.__left_margin

    @left_magin.setter
    def left_margin(self, value: int):
        self.__left_margin = value

    @property
    def background_colour(self):
        """Kolor tła pod napisami.

        Returns:
            [RGB] -- kolor tła pod napisami.
        """
        return self.__background_colour

    @background_colour.setter
    def background_colour(self, value: (int, int, int)):
        self.__background_colour = value

    @property
    def coordinate_x(self):
        """Koordynat x od którego ma być zaczęty
        pisany tekst. Podany w pikselach. Wartość
        mierzona od lewej krawędzi ekranu.

        Returns:
            [int] -- koordynat x.
        """
        return self.__coordinate_x

    @coordinate_x.setter
    def coordinate_x(self, value: int):
        self.__coordinate_x = value
        self.__coordinates = (self.__coordinate_x, self.__coordinate_y)

    @property
    def coordinate_y(self):
        """Koordynat y od którego ma być zaczęty
        pisany tekst. Podany w pikselach. Wartość
        mierzona od górnej krawędzi ekranu.

        Returns:
            [int] -- koordynat y.
        """
        return self.__coordinate_y

    @coordinate_y.setter
    def coordinate_y(self, value: int):
        self.__coordinate_y = value
        self.__coordinates = (self.__coordinate_x, self.__coordinate_y)

    @property
    def coordinates(self):
        """Koordynaty (x,y) wskazujące na których ma zostać
        napisany tekst.

        Returns:
            [int] -- koordynaty
        """
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, value: (int, int)):
        self.__coordinates = value

    @property
    def screen(self):
        """Główny ekran aplikacji.

        Returns:
            [pygame] -- główny ekran aplikacji.
        """
        return self.__screen

    @screen.setter
    def screen(self, value):
        self.__screen = value

    @property
    def font(self):
        """Przygotowana czcionka do renderowania.

        Returns:
            [pygame.font] -- przygotowana czcionka do renderowania.
        """
        return self.__font

    @font.setter
    def font(self, value):
        self.__font = value
