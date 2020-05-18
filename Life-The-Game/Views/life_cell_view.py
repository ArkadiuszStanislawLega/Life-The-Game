"""Autor: Arkadiusz Łęga, email:horemheb@vp.pl"""
import pygame
from Views.view import View
from Library.colours import colours


class LifeCellView(View):
    """Klasa przedstawiająca widok żywej komórki."""

    def __init__(self, screen, model, width=10, height=10):
        """Genruje widok pojedynczej żywej komórki.
        Kożysta z ustawień podanych w argumentach konstruktora.

        Arguments:
            screen {pygame} -- widok głównego okna aplikacji.
            model {LifCell} -- komórka życia używana w klasie Game.

        Keyword Arguments:
            width {int} -- szerokość wioku komórki w pikselach (default: {10})
            height {int} --  wysokość wioku komórki w pikselach (default: {10})
        """
        super().__init__(model=model, name="LifeCellView")
        self.__colour = colours.MATRIX

        self.__width = width
        self.__height = height

        self.__distance_from_the_top = self._model.location.Y * self.__height
        self.__distance_from_the_left = self._model.location.X * self.__width
        self.__coordinates = (self.__distance_from_the_left // 1,
                              self.__distance_from_the_top // 1)

        self.__size = (self.__width, self.__height)
        self.__screen = screen

        self.__position = (self.__coordinates, self.__size)

        self.__body = pygame.draw.ellipse(
            self.__screen, self.__colour, self.__position, 0)

    @property
    def model(self):
        """Komórka życia używana w klasie Game.

        Returns:
            [LifeCell] -- komórka życia.
        """
        return self._model

    @property
    def colour(self):
        """Kolor komórki.

        Returns:
            [RGB] -- kolor komórki.
        """
        return self.__colour

    @colour.setter
    def colour(self, value: (int, int, int)):
        """Pozwala na ustawienie nowego koloru komórki.

        Arguments:
            value {[RGB]} -- nowa wartość dla koloru komórki.
        """
        self.__colour = value

    @property
    def name(self):
        """Nazwa komórki.
        Standardowa nazwa:
        "LifeCell:(0, 0)" - gdzie wartości po ":" są koordynatami
        na których aktualnie znajduje się komórka.

        Returns:
            [str] -- nazwa komórki.
        """
        return self.__name

    @name.setter
    def name(self, value: str):
        """Pozwala na ustawienie nowej nazwy komórki.

        Arguments:
            value {str} -- nowa wartość nazwy komórki.
        """
        self.__name = value

    @property
    def body(self):
        """Ciało komórki wygnerowane przez pygame.

        Returns:
            [pygame] -- widok komórki w oknie.
        """
        return self.__body

    @property
    def width(self):
        """Szerokość widoku komórki w pikselach.

        Returns:
            [int] -- szerokość widoku komórki.
        """
        return self.__width

    @width.setter
    def width(self, value: int):
        """Pozawala na zmianę szeokości widoku komórki.
        Wartość podawana w ilości wyświetlanych piksel.

        Arguments:
            value {int} -- nowa wartość szerokości widoku komórki.
        """
        self.__width = value

    @property
    def height(self):
        """Wysokość widoku komórki, wartość w pikselach.

        Returns:
            [int] -- wysokość widoku komórki.
        """
        return self.__height

    @height.setter
    def height(self, value: int):
        """Pozwala na zmianę wysokości widoku komórki.
        Wartość podawana w ilości wyświetlanych piksel.

        Arguments:
            value {int} -- nowa wartość szerokości widoku komórki.
        """
        self.__height = value

    def add_component(self, comp):
        pass

    def update(self, *args, **kwargs):
        """Aktulizauje pozycje komórki."""
        if len(args) > 0:
            if not self._model.is_alive:
                self.__body = pygame.draw.ellipse(self.__screen,
                                                  colours.BLACK,
                                                  self.__position,
                                                  0)
            else:
                self.__body = pygame.draw.ellipse(self.__screen,
                                                  colours.MATRIX,
                                                  self.__position,
                                                  0)

    def show(self):
        return self.__body
