from Views.view import View
import pygame


class MapCellView(View):
    DARK_RED = (50, 0, 0)
    BLACK = (0, 0, 0)

    def __init__(self, model, screen):
        super().__init__(name="MapCellView", model=model)
        self.__is_was_occupied_colour = self.DARK_RED
        self.__is_was_not_occupied_colour = self.BLACK
        self.__current_colour = self.__is_was_not_occupied_colour
        self.__screen = screen

        self.__width = 10
        self.__height = 10

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
