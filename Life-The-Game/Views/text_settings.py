import pygame
from Library.colours import colours


class TextSettings:
    def __init__(self, screen):
        self.__font_name = 'freesansbold.ttf'
        self.__font_colour = colours.WHITE
        self.__font_size = 12
        self.__left_margin = 15
        self.__background_colour = colours.BLACK
        self.__coordinate_x = self.__left_margin + 0
        self.__coordinate_y = 100
        self.__coordinates = (self.__coordinate_x, self.__coordinate_y)
        self.__screen = screen
        self.__font = pygame.font.Font(self.__font_name, self.__font_size)

    @property
    def font_name(self):
        return self.__font_name

    @font_name.setter
    def font_name(self, value):
        self.__font_name = value

    @property
    def font_colour(self):
        return self.__font_colour

    @font_colour.setter
    def font_colour(self, value):
        self.__font_colour = value

    @property
    def font_size(self):
        return self.__font_size

    @font_size.setter
    def font_size(self, value):
        self.__font_size = value

    @property
    def left_magin(self):
        return self.__left_margin

    @left_magin.setter
    def left_margin(self, value):
        self.__left_margin = value

    @property
    def background_colour(self):
        return self.__background_colour

    @background_colour.setter
    def background_colour(self, value):
        self.__background_colour = value

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
    def coordinates(self):
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, value):
        self.__coordinates = value

    @property
    def screen(self):
        return self.__screen

    @screen.setter
    def screen(self, value):
        self.__screen = value

    @property
    def font(self):
        return self.__font

    @font.setter
    def font(self, value):
        self.__font = value
