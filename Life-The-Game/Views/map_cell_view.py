from Views.view import View
from Library.colours import colours
import pygame


class MapCellView(View):

    def __init__(self, model, screen, width=10, height=10):
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
    def body(self):
        return self.__body

    @property
    def model(self):
        return self._model

    def add_component(self, comp):
        if comp.name not in self._component_list:
            self._component_list[comp.name] = comp

    def update(self, *args, **kwargs):
        if len(kwargs) > 0:
            key = kwargs.get("key")
            value = kwargs.get("value")

            if key == "LifeCell":
                self.model.life_cell = value

        if self._model.is_was_occupied:
            self.__current_colour = self.__is_was_occupied_colour
            self.__body = pygame.draw.rect(
                self.__screen, self.__current_colour, self.__position, 0)

        self.show()

    def show(self):
        return self.__body
