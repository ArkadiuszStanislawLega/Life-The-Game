from Views.view import View
from Views.text_settings import TextSettings
from Views.label_view import LabelView

from Library.colours import colours

import pygame


class TextViews(View):
    """ Klasa jest odpowiedzialna za wyświetlanie napisów w czasie trwania rozgrywki."""

    def __init__(self, model, screen):
        super().__init__(name="TextViews", model=model)
        self.__basic_settings = TextSettings()
        self.__screen = screen

        self.__ROW_HEIGHT = 15
        self.__LEFT_MARGIN = 15
        self.__FONT_NAME = 'freesansbold.ttf'
        self.__FONT_SIZE = 12
        self.__FONT_COLOUR = colours.WHITE
        self.__FONT = pygame.font.Font(self.__FONT_NAME, self.__FONT_SIZE)

        self.__text_print_top_left = []
        self.__text_print_bot_left = []

        self.__unchanging_text()

        self.__background_width = 200
        self.__background_height = 100
        self.__background_coordinates = (5 // 1, 100 // 1)
        self.__background_size = (
            self.__background_width, self.__background_height)
        self.__background_position = (
            self.__background_coordinates, self.__background_size)

        self.__text_background = pygame.draw.rect(
            self.__screen, colours.GRAY, self.__background_position, 0)

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

    def refresh_text_top_left(self):
        """Odświeża dane które wyświetlają się w górnym lewym rogu."""
        texts = [
            f'Umierających komórek: {self._model.dead_cells}',
            f'Żywych komórek:{len(self._model.map.life_cells)}',
            f'Numer rundy: {self._model.current_round}',
            f'Opóźnienie gry: {self._model.settings.current_game_delay}'
        ]

        for text in texts:
            self.add_text_top_left(text)

    def round(self):
        self.show()
        self.refresh_text_top_left()
        self.print_text()
        self.clear_text()

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

        self.__text_background

    def __create_white_text(self, text: str):
        return self.__FONT.render(text, True, self.__FONT_COLOUR)

    def __create_white_text_red_background(self, text: str):
        return self.__FONT.render(text, True, self.__FONT_COLOUR, colours.DARK_RED)

    def add_text_top_left(self, text: str):
        if isinstance(text, str):
            self.__text_print_top_left.append(
                self.__create_white_text(text))

    def add_text_bot_left(self, text: str):
        if isinstance(text, str):
            self.__text_print_bot_left.append(
                self.__create_white_text_red_background(text))

    def clear_text(self):
        """
        Czyści tekst który jest odświerzany co cykl.
        Nie usuwa tekstu który jest statycznie wpisany i nie ulega zmianie.
        """
        self.__text_print_top_left.clear()

    def __unchanging_text(self):
        """
        Dodaje do listy tekstów nie zmieniających się określone informacje.
        """
        self.add_text_bot_left(f'Żeby zatrzymać grę należy wcisnąć SPACJĘ.')
        self.add_text_bot_left(
            f'Żeby ją wznowić należy powtórnie wciśnąć SPCJĘ')
        self.add_text_bot_left(
            f'Do przyspieszenia lub opóźnienia gry należy wciskać +/-')

    def __print_text_top_left(self):
        """
        Drukuje w oknie wszystkie dodane teksty w górnym lewym rogu.
        """
        current_row_height = self.__ROW_HEIGHT
        for text in self.__text_print_top_left:
            self.__screen.blit(text, (self.__LEFT_MARGIN, current_row_height))
            current_row_height += self.__ROW_HEIGHT

    def __print_text_bot_left(self):
        """
        Drukuje w oknie wszystkie dodane teksty w dolnym lewym rogu.
        """
        current_row_height = 1000 - self.__ROW_HEIGHT
        for text in self.__text_print_bot_left:
            self.__screen.blit(text, (self.__LEFT_MARGIN, current_row_height))
            current_row_height -= self.__ROW_HEIGHT

    def __print_backround(self):
        width = 170
        height = len(self.__text_print_top_left) * self.__ROW_HEIGHT + 15

        distance_from_the_top = 10
        distance_from_the_left = 10
        coordinates = (distance_from_the_left // 1, distance_from_the_top // 1)

        size = (width, height)

        position = (coordinates, size)

        pygame.draw.rect(self.__screen, colours.BLACK, position, 0)

    def print_text(self):
        """
        Drukuje wszystkie napisy w oknie.
        """
        self.__print_backround()
        self.__print_text_top_left()
        self.__print_text_bot_left()
