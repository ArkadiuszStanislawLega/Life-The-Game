import pygame

from Library.colours import colours


class ViewSettings:
    def __init__(self, model):
        self.__model = model
        self.__window_title = "Life the game"
        self.__window_background = colours.BLACK
        self.__cell_width = 10
        self.__cell_height = 10
        self.__cell_colour = colours.MATRIX

        self.__window_width = self.__model.game_map.width * self.__cell_width
        self.__window_height = self.__model.game_map.height * self.__cell_height

    @property
    def cell_width(self):
        return self.__cell_width

    @cell_width.setter
    def cell_width(self, value):
        self.__cell_width = value

    @property
    def cell_height(self):
        return self.__cell_height

    @cell_height.setter
    def cell_height(self, value):
        self.__cell_height = value

    @property
    def cell_colour(self):
        return self.__cell_colour

    @cell_colour.setter
    def cell_colour(self, value):
        self.__cell_colour = value

    @property
    def window_title(self):
        return self.__window_title

    @window_title.setter
    def window_title(self, value):
        self.__window_title = value

    @property
    def window_background(self):
        return self.__window_background

    @window_background.setter
    def window_background(self, value):
        self.__window_background = value

    @property
    def window_width(self):
        return self.__window_width

    @property
    def window_height(self):
        return self.__window_height

    @property
    def window_size(self):
        return (self.__window_width, self.__window_height)
