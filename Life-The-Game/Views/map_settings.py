import pygame

from Library.colours import colours


class MapSettings:
    def __init__(self, cell_width=10, cell_height=10):
        self.__cell_width = cell_width
        self.__cell_height = cell_height
        self.__cell_colour = colours.MATRIX

    @property
    def cell_width(self):
        return self.__cell_width

    @property
    def cell_height(self):
        return self.__cell_height

    @property
    def cell_colour(self):
        return self.__cell_colour

    @cell_colour.setter
    def cell_colour(self, value):
        self.__cell_colour = value
