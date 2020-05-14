from Views.view import View
from Views.text_settings import TextSettings
from Views.label_view import LabelView

import pygame


class TextViews(View):
    """ Klasa jest odpowiedzialna za wyświetlanie napisów w czasie trwania rozgrywki."""

    def __init__(self, model, screen):
        super().__init__(name="TextViews", model=model)
        self.__basic_settings = TextSettings()
        self.__screen = screen

        self.__game_delay_info = LabelView(self.__screen,
                                           self._model.settings.current_game_delay,
                                           "Aktulna prędkość rozgrywki: ",
                                           "LabelView_game_delay")

        self.__life_cell_info = LabelView(self.__screen,
                                          len(self._model.map.life_cells),
                                          "Żywe komórki: ",
                                          "LabelView_life_cells")

        self.__current_number_of_round_info = LabelView(self.__screen,
                                                        self._model.current_round,
                                                        "Numer rundy: ",
                                                        "LabelView_round_number")

        self.__life_cell_info.settings.coordinate_y = self.__game_delay_info.settings.coordinate_y + 15
        self.__current_number_of_round_info.settings.coordinate_y = self.__life_cell_info.settings.coordinate_y + 15

        self._model.add_observer(self.__game_delay_info)
        self._model.add_observer(self.__life_cell_info)
        self._model.add_observer(self.__current_number_of_round_info)

        self.add_component(self.__game_delay_info)
        self.add_component(self.__life_cell_info)
        self.add_component(self.__current_number_of_round_info)

    @property
    def info_game_delay(self):
        return self._component_list.get("LabelView_game_delay")

    def add_component(self, comp):
        if comp.name not in self._component_list:
            self._component_list[comp.name] = comp

        self.show()

    def update(self, *args, **kwargs):
        for view in self._component_list.values():
            view.update()

    def show(self):
        for view in self._component_list.values():
            view.show()
