from Views.view import View
from Library.colours import colours

import pygame


class LifeCellView(View):
    """Klasa przedstawiająca widok żywej komórki."""

    def __init__(self, screen, model, width=10, height=10):
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

        self.__screen_surface = pygame.display.get_surface().get_size()
        self.__right_border = self.__screen_surface[0]
        self.__bot_border = self.__screen_surface[1]

    @property
    def model(self):
        return self._model

    @property
    def colour(self):
        return self.__colour

    @colour.setter
    def colour(self, value):
        self.__colour = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def body(self):
        return self.__body

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def distance_from_the_top(self):
        return self.__distance_from_the_top

    @property
    def distance_from_the_left(self):
        return self.__distance_from_the_left

    @property
    def position(self):
        return self.__position

    def add_component(self, comp):
        pass

    def update(self, *args, **kwargs):
        """Aktulizauje pozycje komórki."""
        if len(args) > 0:
            self._model = args[0]
            if self._model.is_alive:
                self.__body = pygame.draw.ellipse(
                    self.__screen, self.__colour, self.__position, 0)
                self.show()
            else:
                self.__body = pygame.draw.ellipse(
                    self.__screen, colours.WHITE, self.__position, 0)
                self.show()

    def show(self):
        return self.__body
