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
        self.__settings = TextSettings(self.__screen)
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

    def udpate_body(self):
        self.__body = self.__settings.font.render(self.__full_text,
                                                  False,
                                                  self.__settings.font_colour)
        return self.__body

    def update(self, *args, **kwargs):
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "game_delay":
                    self._model = value
                    self.__full_text = f'{self.__text}{self._model}'
                    self.__body = self.__settings.font.render(self.__full_text,
                                                              True,
                                                              self.__settings.font_colour,
                                                              self.__settings.background_colour)

                if key == "LabelView_life_cells":
                    self._model = value
                    self.__full_text = f'{self.__text}{self._model}'
                    self.__body = self.__settings.font.render(self.__full_text,
                                                              True,
                                                              self.__settings.font_colour,
                                                              self.__settings.background_colour)

    def show(self):
        self.__screen.blit(self.__body, self.__settings.coordinates)
