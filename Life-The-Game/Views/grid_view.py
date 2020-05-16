from Views.view import View
from Views.text_settings import TextSettings
from Views.label_view import LabelView
from Library.colours import colours
import pygame


class GridView(View):
    def __init__(self, screen, name="GridView", lenght_from_top=0, labels={}, row_height=15, first_element_on_top=True):
        """
        Widok grida, ustawia komponenty wchodzące w jego skład od góry do dołu jeden po drugim,
        lub od dołu do góry.

        Arguments:
            View {View} -- Klasa którą powinien dziedziczyć każdy element widoku gry.
            screen {pygame} -- Instancja okna gry.

        Keyword Arguments:
            name {str} -- Nazwa grida, po której będzie można go wyszukać w widokach rodzicach. (default: {"GridView"})
            lenght_from_top {int} -- Wysokość od której ma zacząc rysować komponenty grida. (default: {0})
            labels {dict} -- Komponenty wchodzące w skład girda (default: {{str: LabelView}})
            row_height {int} -- Wysokość jednego wiersza w gridzie (default: {15})
            first_element_on_top {bool} -- Flaga wskazująca czy pierwszy element z kompnentów 
                                           wchodzących w skład grida, będzie pierwszy od góry, czy pierwsz od dołu. 
                                           (default: {True})
        """
        super().__init__(model=None, name=name)
        # Dodawanie kolejnych elementów, pierwszy element na dole, czy u góry.
        self.__first_element_on_top = first_element_on_top
        self.__row_height = row_height
        self.__screen = screen
        self.__lenght_from_top = lenght_from_top
        self._component_list = labels

        self.__add_coordinates_to_components()

    def __add_coordinates_to_components(self):
        """Przydziela odpowiednie koordynaty komponentom wchodzącym w skład grida."""
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
