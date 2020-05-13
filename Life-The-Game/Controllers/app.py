from Models.game import Game

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
        self.__delay_counter = 0
        self.__default_game_delay = 1
        self.__user_game_delay = 1
        self.__is_user_change_delay = False
        self.__current_game_delay = 1
        # Flaga wskazująca czy przycisk spacji był wciśnięty
        self.__is_space_pushed = False
        self.__is_working = True
        self.__clock = pygame.time.Clock()

        self.__game = Game(map_width=self.GAME_WIDTH,
                           map_height=self.GAME_HEIGHT)

        self.__game_view = GameView(self.__game)
        self.__game.add_observer(self.__game_view)

        self.__info_game_delay_view = InfoGameDelayView(screen=self.__game_view.screen,
                                                        model=self.__current_game_delay)

        self.__event_controller = EventsController(
            view=self.__game_view, model=self)

        self.__text_view = TextView(
            model=self.__game, screen=self.__game_view.screen)

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

    @info_game_delay_view.setter
    def info_game_delay_view(self, view):
        self.__info_game_delay_view = view

    @property
    def default_game_delay(self):
        return self.__default_game_delay

    @default_game_delay.setter
    def default_game_delay(self, value):
        self.__default_game_delay = value

    @property
    def user_game_delay(self):
        return self.__user_game_delay

    @user_game_delay.setter
    def user_game_delay(self, value):
        self.__user_game_delay = value

    @property
    def is_user_change_delay(self):
        return self.__is_user_change_delay

    @is_user_change_delay.setter
    def is_user_change_delay(self, value):
        self.__is_user_change_delay = value

    @property
    def is_space_pushed(self):
        return self.__is_space_pushed

    @is_space_pushed.setter
    def is_space_pushed(self, value):
        self.__is_space_pushed = value

    @property
    def current_game_delay(self):
        return self.__current_game_delay

    @current_game_delay.setter
    def current_game_delay(self, value):
        self.__current_game_delay = value

    @property
    def delay_counter(self):
        return self.__delay_counter

    @delay_counter.setter
    def delay_counter(self, value):
        self.__delay_counter = value

    @property
    def is_working(self):
        return self.__is_working

    @is_working.setter
    def is_working(self, value):
        self.__is_working = value

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
            f'Opóźnienie gry: {self.__current_game_delay}')

    def start_game(self):
        """
        Inicjalizuje grę.
        Zawarta tutaj jest główna pętla aplikacji.
        """
        while self.__is_working:

            self.__event_controller.get_input()

            self.__game_controller.get_input()
            self.__delay_counter += 1

            self.__refresh_text_top_left()

            if self.__delay_counter == self.__current_game_delay:
                self.__game.run()
                self.__delay_counter = 0

            self.__text_view.show()
            self.__text_view.clear_text()

            self.__clock.tick(self.REFRESH_RATE)
            pygame.display.flip()

        pygame.quit()
