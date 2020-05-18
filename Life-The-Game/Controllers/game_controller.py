"""Autor: Arkadiusz Łęga, email:horemheb@vp.pl"""
import pygame

from Controllers.controller import Controller
from Controllers.events_controller import EventsController


class GameController(Controller):
    """
    Inicuje wszystkie kontrolery potrzebne do przeprowadzenia rozgrywki.

    Arguments:
        Controller {Controller} -- Interfejs umożliwający połączenie widoku z modelem.
    """

    def __init__(self, view, model, refresh_rate=60):
        """
        Inicjuje częstotliwość odświeżania oraz Clock, oraz tworzy instancję klasy
        odpowiedzialnej za przechwytwanie zdarzeń wciśnięć klawiszy w klawiaturze.

        Arguments:
            view {View} -- Widok do którego mają zostać przekazane wprowadzone zmiany.
            model {[type]} -- Model z którego są pobierane dane do wyświetlenia użytkownikowi.

        Keyword Arguments:
            refresh_rate {int} -- Częstotliwość odświeżania ilość klatek/s (default: {60})
        """
        super().__init__(view=view, model=model)
        self.__refresh_rate = refresh_rate
        self.__clock = pygame.time.Clock()

        self.__events = EventsController(view=self._view, model=self._model)

    def start_game(self):
        """
        Inicjalizuje grę.
        Zawarta tutaj jest główna pętla aplikacji.
        """
        self._model.cells_at_the_begginning()

        while self._model.is_working:
            self.__events.get_input()
            self._model.settings.delay_counter += 1

            if self._model.settings.delay_counter == self._model.settings.current_game_delay:
                self._model.run()
                self._model.settings.delay_counter = 0

            self._view.round()

            self.__clock.tick(self.__refresh_rate)
            pygame.display.flip()

        pygame.quit()

    def get_input(self):
        pass
