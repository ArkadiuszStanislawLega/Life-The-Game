"""Autor: Arkadiusz Łęga, email:horemheb@vp.pl
*******************************************************************************

Można by doprawcować wyświetlanie i aktualizacje widoków, ale niestety czas mi
nie pozwoli na dopracowanie tego elementu.

*******************************************************************************
"""
import pygame
from Views.view import View
from Views.text_settings import TextSettings
from Views.label_view import LabelView
from Views.grid_view import GridView


class TextViews(View):
    """ Klasa jest odpowiedzialna za wyświetlanie napisów w czasie trwania rozgrywki."""
    MARGIN_TOP = 10

    def __init__(self, model, screen):
        """Ustawia podstawowe wartość widoku wszystkich tekstów w casie rozgrywki.

        Arguments:
            model {Game} -- instancja klasy Game która prowadzi całą rozgrywkę.
            screen {pygame} -- główny widok aplikacji.
        """
        super().__init__(name="TextViews", model=model)
        screen_width, screen_height = pygame.display.get_surface().get_size()
        self.__screen = screen
        self.__bot_grid_components = {
            "LabelView_text_1": LabelView(self.__screen,
                                          "",
                                          f'Żeby ją wznowić należy powtórnie wciśnąć SPCJĘ',
                                          "LabelView_text_1"),
            "LabelView_text_2": LabelView(self.__screen,
                                          "",
                                          f'Żeby zatrzymać grę należy wcisnąć SPACJĘ.',
                                          "LabelView_text_2"),
            "LabelView_text_3": LabelView(self.__screen,
                                          "",
                                          f'Do przyspieszenia lub opóźnienia gry należy wciskać +/-',
                                          "LabelView_text_3")
        }

        self.__grid_bot = GridView(screen=screen,
                                   name="Grid_bot",
                                   first_element_on_top=False,
                                   lenght_from_top=screen_height,
                                   labels=self.__bot_grid_components)

        self.__basic_settings = TextSettings()
        self.__row_height = 15
        self.add_component(self.__grid_bot)
        self.add_labels()
        self.grid()

    @property
    def info_game_delay(self):
        """Zwraca widok który wyświetla aktualne opóźnienie gry.

        Returns:
            [LabelView] -- widok aktualnego opóźnienienia gry.
        """
        return self._component_list.get("LabelView_game_delay")

    def add_labels(self):
        """Dodaje wszystkie widoki po lewej górenj części ekranu."""
        self.add_component(LabelView(self.__screen,
                                     self._model.dead_cells,
                                     "Umierających komórek: ",
                                     "LabelView_dead_cells"))
        self.add_component(LabelView(self.__screen,
                                     len(self._model.map.life_cells),
                                     "Żywe komórki: ",
                                     "LabelView_life_cells"))
        self.add_component(LabelView(self.__screen,
                                     self._model.current_round,
                                     "Numer rundy: ",
                                     "LabelView_round_number"))
        self.add_component(LabelView(self.__screen,
                                     self._model.settings.current_game_delay,
                                     "Aktulna prędkość rozgrywki: ",
                                     "LabelView_game_delay"))

    def grid(self):
        """Tworzy kontener z widokami napisów. Zachowując dystans od
        góry podany jakos stała MARGIN_TOP zainicjalizowany przy deklaracji
        tej klasy."""
        coordinate_y = self.MARGIN_TOP
        current_coordinate_y = coordinate_y
        for view in self._component_list.values():
            if isinstance(view, LabelView):
                view.settings.coordinate_y = current_coordinate_y
                current_coordinate_y += self.__row_height

    def update_labels(self):
        """Aktualizuje dane pobrane z instancji Game zarządzającej rozgrywką."""
        dead_cells = self._component_list.get("LabelView_dead_cells")
        life_cells = self._component_list.get("LabelView_life_cells")
        round_number = self._component_list.get("LabelView_round_number")
        game_delay = self._component_list.get("LabelView_game_delay")

        dead_cells.update(self._model.dead_cells)
        life_cells.update(len(self._model.map.life_cells))
        game_delay.update(self._model.settings.current_game_delay)
        round_number.update(self._model.current_round)

    def refresh_grid(self):
        """Odświeża widoki napisów."""
        self.update_labels()
        for view in self._component_list.values():
            view.show()

    def round(self):
        """Zadania wchodzące wskład akcji wykonywanych raz na rundę rozgrywki."""
        self.refresh_grid()
        self.show()

    def add_component(self, comp):
        if comp.name not in self._component_list:
            self._component_list[comp.name] = comp

    def update(self, *args, **kwargs):
        for view in self._component_list.values():
            view.update()

    def show(self):
        for view in self._component_list.values():
            view.show()
