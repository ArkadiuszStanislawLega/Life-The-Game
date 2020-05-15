import pygame

from Controllers.controller import Controller
from Controllers.events_controller import EventsController

from Models.game_settings import GameSettings


class GameController(Controller):
    def __init__(self, view, model):
        super().__init__(view=view, model=model)
        self.__refresh_rate = 60
        self.__clock = pygame.time.Clock()

        self.__events = EventsController(view=self._view, model=self._model)

    def __refresh_text_top_left(self):
        """
        Odświeża dane które wyświetlają się w górnym lewym rogu.
        """
        self._view.texts.add_text_top_left(
            f'Umierających komórek: ')

        self._view.texts.add_text_top_left(
            f'Żywych komórek:')

        self._view.texts.add_text_top_left(
            f'Numer rundy: ')

        self._view.texts.add_text_top_left(
            f'Opóźnienie gry: ')

    def start_game(self):
        """
        Inicjalizuje grę.
        Zawarta tutaj jest główna pętla aplikacji.
        """
        self._model.cells_at_the_begginning()

        while self._model.is_working:
            self.__events.get_input()
            self._view.texts.show()
            self._model.settings.delay_counter += 1

            self.__refresh_text_top_left()

            if self._model.settings.delay_counter == self._model.settings.current_game_delay:
                self._model.run()
                self._model.settings.delay_counter = 0
            self._view.map.remove_dead_cells_views()

            self.__clock.tick(self.__refresh_rate)
            self._view.texts.print_text()
            self._view.texts.clear_text()
            pygame.display.flip()

        pygame.quit()

    def get_input(self):
        pass
