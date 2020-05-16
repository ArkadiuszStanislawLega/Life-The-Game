from Views.view import View
from Views.text_settings import TextSettings
from Views.label_view import LabelView
from Library.colours import colours
import pygame


class GridView(View):
    def __init__(self, screen, name="GridView", lenght_from_top=0, labels={}, row_height=15, first_element_on_top=True):
        super().__init__(model=None, name=name)
        # Dodawanie kolejnych elementów, pierwszy element na dole, czy u góry.
        self.__first_element_on_top = first_element_on_top
        self.__row_height = row_height
        self.__screen = screen
        self.__lenght_from_top = lenght_from_top
        self._component_list = labels

        self.grid()

    def grid(self):
        coordinate_y = self.__lenght_from_top
        current_coordinate_y = coordinate_y

        for view in self._component_list.values():
            if isinstance(view, LabelView):
                if self.__first_element_on_top:
                    current_coordinate_y += self.__row_height
                else:
                    current_coordinate_y -= self.__row_height

                view.settings.coordinate_y = current_coordinate_y

    def add_component(self, comp: View):
        if isinstance(comp, View):
            if comp.name not in self._component_list:
                self._component_list[comp.name] = comp

    def update(self, *args, **kwargs):
        for view in self._component_list.values():
            view.update()

    def show(self):
        for view in self._component_list.values():
            view.show()
