from Views.view import View
from Views.text_settings import TextSettings
from Library.colours import colours
import pygame


class LabelView(View):
    def __init__(self, screen, model=1, text="", name="LabelView"):
        super().__init__(name=name, model=model)
        self.__screen = screen
        self.__text = text
        self.__full_text = f'{self.__text}{self._model}'
        self.__settings = TextSettings()
        self.__body = self.__settings.font.render(self.__full_text,
                                                  False,
                                                  self.__settings.font_colour)

    @property
    def settings(self):
        return self.__settings

    @settings.setter
    def settings(self, value):
        self.__settings = value

    def add_component(self, comp):
        if comp.name not in self._component_list:
            self._component_list[comp.name] = comp

    def update(self, *args, **kwargs):
        if len(args) > 0:
            self._model = args[0]
            self.__full_text = f'{self.__text}{self._model}'
            self.__body = self.__settings.font.render(self.__full_text,
                                                      True,
                                                      self.__settings.font_colour,
                                                      self.__settings.background_colour)

    def show(self):
        self.__body = self.__settings.font.render(self.__full_text,
                                                  True,
                                                  self.__settings.font_colour,
                                                  self.__settings.background_colour)

        self.__screen.blit(self.__body, (self.__settings.left_margin,
                                         self.__settings.coordinate_y))
