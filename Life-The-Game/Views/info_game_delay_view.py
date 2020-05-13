from Views.view import View
from Library.colours import colours
import pygame


class InfoGameDelayView(View):
    def __init__(self, screen, model):
        super().__init__(name="InfoGameDelayView", model=model)
        self.__font_name = 'freesansbold.ttf'
        self.__font_colour = colours.WHITE
        self.__font_size = 12
        self.__left_margin = 15
        self.__text = f'Opóźnienie gry: {self._model}'
        self.__background_colour = colours.BLACK
        self.__coordinate_x = self.__left_margin + 0
        self.__coordinate_y = 130
        self.__coordinates = (self.__coordinate_x, self.__coordinate_y)
        self.__screen = screen
        self.__font = pygame.font.Font(self.__font_name, self.__font_size)
        self.__body = self.__font.render(
            self.__text, True, self.__font_colour, self.__background_colour)

    @property
    def coordinate_x(self):
        return self.__coordinate_x

    @coordinate_x.setter
    def coordinate_x(self, value):
        self.__coordinate_x = value

    @property
    def coordinate_y(self):
        return self.__coordinate_y

    @coordinate_y.setter
    def coordinate_y(self, value):
        self.__coordinate_y = value

    @property
    def background_colour(self):
        return self.__background_colour

    @background_colour.setter
    def background_colour(self, value):
        self.__background_colour = value

    def add_component(self, comp):
        if comp.name not in self._component_list:
            self._component_list[comp.name] = comp

    def update(self, *args, **kwargs):
        self.__text = f'Opóźnienie gry: {self._model}'
        self.__body = self.__font.render(
            self.__text, True, self.__font_colour, self.__background_colour)

    def show(self):
        self.__screen.blit(self.__body, self.__coordinates)
