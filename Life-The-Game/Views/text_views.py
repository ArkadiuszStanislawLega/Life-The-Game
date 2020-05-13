from Views.view import View
from Views.text_settings import TextSettings
from Views.label_view import LabelView

import pygame


class TextViews(View):
    """ Klasa jest odpowiedzialna za wyświetlanie napisów w czasie trwania rozgrywki."""

    def __init__(self, model, screen):
        super().__init__(name="TextViews", model=model)
        self.__basic_settings = TextSettings(screen=screen)
        self.__screen = screen

        self.__game_delay_info = LabelView(self.__screen,
                                           self._model.settings.current_game_delay,
                                           "Aktulna prędkość rozgrywki: ",
                                           "LabelView_game_delay")

        self.__life_cell_info = LabelView(self.__screen,
                                          len(self._model.life_cells),
                                          "Żywe komórki: ",
                                          "LabelView_life_cells")

        self.__life_cell_info.settings.coordinate_y = self.__game_delay_info.settings.coordinate_y + 15

        self.add_component(self.__game_delay_info)
        self.add_component(self.__life_cell_info)

    @property
    def info_game_delay(self):
        return self._component_list.get("LabelView_game_delay")

    def add_component(self, comp):
        if comp.name not in self._component_list:
            self._component_list[comp.name] = comp

        self.show()

    def update(self, *args, **kwargs):
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if self._component_list.get(key):
                    value.udpate()
                    value.show()

    def show(self):
        for view in self._component_list.values():
            view.show()
