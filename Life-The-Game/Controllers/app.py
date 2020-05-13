from Models.game import Game
from Models.game_setting import GameSettings

from Controllers.game_controller import GameController
from Controllers.events_controller import EventsController

from Views.texts_view import TextView
from Views.game_view import GameView

from Views.info_game_delay_view import InfoGameDelayView
import pygame


class App():
    """
    Klasa łącząca model - widok - kontrolery.
    Przy takich ustawieniach mapa działa na cały ekran przy rozdzielczości 1366x768 ekran 15"
    GAME_WIDTH = 137
    GAME_HEIGHT = 73
    """

    GAME_WIDTH = 137
    GAME_HEIGHT = 73

    REFRESH_RATE = 60

    def __init__(self):

        self.__clock = pygame.time.Clock()

        self.__game = Game(map_width=self.GAME_WIDTH,
                           map_height=self.GAME_HEIGHT)
        self.__view = GameView(self.__game)

        self.__settings = GameSettings()

        self.__game.add_observer(self.__view)

        self.__info_game_delay_view = InfoGameDelayView(screen=self.__view.screen,
                                                        model=self.__settings.current_game_delay)

        self.__event_controller = EventsController(
            view=self.__view, model=self)

        self.__text_view = TextView(
            model=self.__game, screen=self.__view.screen)

        self.__text_view.add_component(self.__info_game_delay_view)

        self.__game.add_observer(self.__text_view)

        self.__game_controller = GameController(
            model=self.__game, view=self.__text_view)

        self.__game.cells_at_the_begginning()
        self.__text_view.show()
        self.start_game()

    @property
    def info_game_delay_view(self):
        return self.__info_game_delay_view

    @property
    def text_view(self):
        return self.__text_view

    @property
    def game(self):
        """Instancja modelu obsługującą mechanikę gry."""
        return self.__game

    def __refresh_text_top_left(self):
        """
        Odświeża dane które wyświetlają się w górnym lewym rogu.
        """
        self.__text_view.add_text_top_left(
            f'Umierających komórek: {self.__game.dead_cells}')

        self.__text_view.add_text_top_left(
            f'Żywych komórek: {len(self.__game.life_cells)}')

        self.__text_view.add_text_top_left(
            f'Numer rundy: {self.__game.current_round}')

        self.__text_view.add_text_top_left(
            f'Opóźnienie gry: {self.__settings.current_game_delay}')

    def start_game(self):
        """
        Inicjalizuje grę.
        Zawarta tutaj jest główna pętla aplikacji.
        """
        while self.__settings.is_working:

            self.__event_controller.get_input()

            self.__game_controller.get_input()
            self.__settings.delay_counter += 1

            self.__refresh_text_top_left()

            if self.__settings.delay_counter == self.__settings.current_game_delay:
                self.__game.run()
                self.__delay_counter = 0

            self.__text_view.show()
            self.__text_view.clear_text()

            self.__clock.tick(self.REFRESH_RATE)
            pygame.display.flip()

        pygame.quit()
