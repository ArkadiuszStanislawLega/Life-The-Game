from Views.view import View

import pygame


class CellView(View):
    def __init__(self, screen, model):
        super().__init__(model=model, name="CellView")
        self.__colour = (0, 0, 0)
        self.__distance_from_the_top = 10
        self.__distance_from_the_left = 10
        self.__coordinates = (self.__distance_from_the_left // 2,
                              self.__distance_from_the_top // 2)

        self.__width = 10
        self.__height = 10
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
        return self._model.name

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
        """
        Aktulizauje pozycje komórki.
        """
        self.__distance_from_the_top = self._model.location.X * self.__width
        self.__distance_from_the_left = self._model.location.Y * self.__height

        self.__coordinates = (self.__distance_from_the_top // 1,
                              self.__distance_from_the_left // 1)

        self.__position = (self.__coordinates, self.__size)

        self.__body = pygame.draw.ellipse(
            self.__screen, self.__colour, self.__position, 0)

    def show(self):
        pass
