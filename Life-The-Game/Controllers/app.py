from Models.game import Game
from Models.life_cell import LifeCell
from Models.location import Location
from Views.game_view import GameView
import pygame
import sys


class App():

    # Przy takich ustawieniach mapa działa na cały ekran przy rozdzielczości 1366x768 ekran 15"
    GAME_WIDTH = 137
    GAME_HEIGHT = 73

    REFRESH_RATE = 60

    def __init__(self):
        self.__game = Game(map_width=self.GAME_WIDTH,
                           map_height=self.GAME_HEIGHT)

        self.__game_view = GameView(self.__game)
        self.__game.add_observer(self.__game_view)

        self.__clock = pygame.time.Clock()

        self.__current_game_delay = 1
        self.__default_game_delay = 1
        self.__user_game_delay = 1
        self.__is_user_change_delay = False

        self.__delay_counter = 0
        self.__is_working = True

        self.__is_space_pushed = False

        self.__game.cells_at_the_begginning()
        self.start_game()

    def __refresh_text_top_left(self):
        """
        Odświeża dane które wyświetlają się w górnym lewym rogu.
        """
        self.__game_view.add_text_top_left(
            f'Umierających komórek: {self.__game.dead_cells}')

        self.__game_view.add_text_top_left(
            f'Żywych komórek: {len(self.__game.life_cells)}')

        self.__game_view.add_text_top_left(
            f'Numer rundy: {self.__game.current_round}')

        self.__game_view.add_text_top_left(
            f'Opóźnienie gry: {self.__current_game_delay}')

    def start_game(self):
        """
        Inicjalizuje grę. 
        Zawarta tutaj jest główna pętla aplikacji.
        """
        while self.__is_working:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__is_working = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.__is_space_pushed:
                            if self.__is_user_change_delay:
                                self.__current_game_delay = self.__user_game_delay
                            else:
                                self.__current_game_delay = self.__default_game_delay

                            self.__delay_counter = 0
                            self.__is_space_pushed = False
                        else:
                            self.__current_game_delay = -1
                            self.__is_space_pushed = True
                            self.__game_view.print_text()

                    if event.key == pygame.K_KP_PLUS or event.key == pygame.K_PLUS:
                        self.__is_user_change_delay = True
                        self.__user_game_delay += 1
                        self.__delay_counter = 0
                        self.__current_game_delay = self.__user_game_delay

                    if event.key == pygame.K_KP_MINUS or event.key == pygame.K_MINUS:
                        self.__is_user_change_delay = True
                        if self.__user_game_delay > 1:
                            self.__user_game_delay -= 1
                            self.__delay_counter = 0
                            self.__current_game_delay = self.__user_game_delay

            # self.__game_view.screen.fill(self.__game_view.window_background)

            self.__delay_counter += 1

            self.__refresh_text_top_left()

            if self.__delay_counter == self.__current_game_delay:
                self.__game.run()
                self.__game_view.round()
                self.__delay_counter = 0

            self.__game_view.show()
            # self.__game_view.print_all_live_cells()
            self.__game_view.print_text()
            self.__game_view.clear_text()

            self.__clock.tick(self.REFRESH_RATE)
            pygame.display.flip()

        pygame.quit()
