"""Autor: Arkadiusz Łęga, email:horemheb@vp.pl"""
import pygame
from Views.view import View
from Library.colours import colours


class MapCellView(View):
    """Klasa reprezentująca pojedynczą komórkę mapy."""

    def __init__(self, model, screen, width=10, height=10):
        """Genruje widok pojedynczej komórki mapy.
        Kożysta z ustawień podanych w argumentach konstruktora.

        Arguments:
            model {MapCell} -- komórka mapy z mechaniki gry w instancji
                                Game, która steruje całą rozgrywką.
            screen {pygame} -- główne okno aplikacji.

        Keyword Arguments:
            width {int} -- szerokość widoku komórki podana w pikselach (default: {10})
            height {int} -- wysokość widoku komórki podana w pikselach (default: {10})
        """
        super().__init__(name="MapCellView", model=model)
        self.__is_was_occupied_colour = colours.DARK_RED
        self.__is_was_not_occupied_colour = colours.BLACK
        self.__current_colour = self.__is_was_not_occupied_colour
        self.__screen = screen

        self.__width = width
        self.__height = height

        self.__distance_from_the_top = self._model.location.Y * self.__height
        self.__distance_from_the_left = self._model.location.X * self.__width

        self.__coordinates = (self.__distance_from_the_left // 1,
                              self.__distance_from_the_top // 1)

        self.__size = (self.__width, self.__height)
        self.__position = (self.__coordinates, self.__size)

        self.__body = pygame.draw.rect(
            self.__screen, self.__current_colour, self.__position, 0)
        self._name += f':{self._model.location}'

    @property
    def width(self):
        """Szerokość widoku komórki w pikselach.

         Returns:
             [int] -- szerokość widoku komórki.
         """
        return self.__width

    @width.setter
    def width(self, value):
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
    def height(self, value):
        """Pozwala na zmianę wysokości widoku komórki.
        Wartość podawana w ilości wyświetlanych piksel.

        Arguments:
            value {int} -- nowa wartość szerokości widoku komórki.
        """
        self.__height = value

    @property
    def body(self):
        """Ciało komórki wygnerowane przez pygame.

        Returns:
            [pygame] -- widok komórki w oknie.
        """
        return self.__body

    @property
    def model(self):
        """Model komórki używany w mapie w instancji Game
        która steruje rozgrywką.

        Returns:
            [MapCell] -- komórka mapy z instancji Game.
        """
        return self._model

    def add_component(self, comp):
        if comp.name not in self._component_list:
            self._component_list[comp.name] = comp

    def update(self, *args, **kwargs):
        if len(args) > 0:
            self._model = args[0]
            if self._model.is_was_occupied:
                self.__current_colour = self.__is_was_occupied_colour
                self.__body = pygame.draw.rect(self.__screen,
                                               self.__current_colour,
                                               self.__position,
                                               0)

    def show(self):
        return self.__body
