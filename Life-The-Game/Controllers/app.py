from Models.game import Game
from Models.life_cell import LifeCell
from Models.location import Location
from Library.demonid import demonid
from Library.glider import glider
from Library.horizontal_line import horizontal_line
from Library.spaceship import spaceship
from Library.noah_ark import noah_ark
from Library.info import struct_info
from Views.cell_view import CellView
import random
import pygame
import sys
import datetime


class App():
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    GRAY = (192, 192, 192)
    DARKRED = (139, 0, 0)
    MATRIX = (52, 195, 5)

    REFRESH_RATE = 60

    COLOUR_BACKGROUND = BLACK
    COLOUR_CELLS = MATRIX
    COLOUR_TEXT = WHITE
    COLOUT_TEXT_BACKGROUD = COLOUR_BACKGROUND

    FONT_SIZE = 12
    FONT_NAME = 'freesansbold.ttf'

    GAME_WIDTH = 120
    GAME_HEIGHT = 60

    CELLS_WIDTH = 10
    CELLS_HEIGHT = 10

    WINDOW_WIDTH = GAME_WIDTH*CELLS_WIDTH
    WINDOW_HEIGHT = GAME_HEIGHT*CELLS_HEIGHT

    WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
    WINDOW_TITLE = "Life the game"

    def __init__(self):
        self.__start_time = datetime.datetime.now()
        self.__number_of_rounds = 0
        self.__cells = {}
        self.__keys_of_dead_cells = []
        self.__number_of_dead_cells = 0
        self.__screen = pygame.display.set_mode(self.WINDOW_SIZE)
        self.__clock = pygame.time.Clock()

        self.__current_game_delay = 1
        self.__default_game_delay = 1
        self.__user_game_delay = 1
        self.__is_user_change_delay = False

        self.__delay_counter = 0
        self.__is_working = True
        # Instancja gry - mechanika działania
        self.__game = Game(map_width=self.GAME_WIDTH,
                           map_height=self.GAME_HEIGHT)
        self.__is_space_pushed = False

        self.__cells_at_the_begginning()

        self.start_game()

    def gen_random_x(self, struc_info: dict):
        return random.randrange(0, self.GAME_WIDTH-struc_info.get("width"))

    def gen_random_y(self, struc_info: dict):
        return random.randrange(0, self.GAME_HEIGHT-struc_info.get("height"))

    def generate_random_demonid(self):
        demonid_info = struct_info().get("demonid")
        demonid(self.__game, self.gen_random_x(
            demonid_info), self.gen_random_y(demonid_info))

    def generate_random_spaceship(self):
        spaceship_info = struct_info().get("spaceship")
        spaceship(self.__game, self.gen_random_x(
            spaceship_info), self.gen_random_y(spaceship_info))

    def generate_random_glider(self):
        glider_info = struct_info().get("glider")
        glider(self.__game, self.gen_random_x(
            glider_info), self.gen_random_y(glider_info))

    def generate_random_noah_ark(self):
        noah_ark_info = struct_info().get("noah_ark")
        noah_ark(self.__game, self.gen_random_x(
            noah_ark_info), self.gen_random_y(noah_ark_info))

    def __cells_at_the_begginning(self):
        """
        Początkowy układ komórek przy uruchomieniu aplikacji.
        """
        self.generate_random_demonid()
        self.generate_random_spaceship()
        self.generate_random_demonid()
        # self.generate_random_spaceship()
        self.generate_random_demonid()
        # self.generate_random_spaceship()

        self.generate_random_glider()
        self.generate_random_glider()
        self.generate_random_glider()
        self.generate_random_glider()

        self.generate_random_noah_ark()

        # demonid(self.__game, 1, 5)
        # demonid(self.__game, 23, 5)
        # demonid(self.__game, 46, 5)
        # demonid(self.__game, 70, 5)

        # demonid(self.__game, 1, 20)
        # demonid(self.__game, 23, 20)
        # demonid(self.__game, 46, 20)
        # demonid(self.__game, 70, 20)

        # demonid(self.__game, 1, 35)
        # demonid(self.__game, 23, 35)
        # demonid(self.__game, 46, 35)
        # demonid(self.__game, 70, 35)

        #spaceship(self.__game, 60, 20)

        # glider(self.__game, 10, 10)
        # glider(self.__game, 20, 10)
        # glider(self.__game, 30, 10)
        # glider(self.__game, 40, 10)

        #noah_ark(self.__game, 20, 30)

    def __add_new_cells(self):
        """
        Dodaje wszystkie widoki komórek które są utworzone w instancji gry.
        """
        for key, value in self.__game.life_cells.items():
            if not self.__cells.get(key):
                new_cell = CellView(self.__screen, value)
                new_cell.width = self.CELLS_WIDTH
                new_cell.height = self.CELLS_HEIGHT
                new_cell.colour = self.COLOUR_CELLS
                self.__cells.update({key: new_cell})

    def __make_list_of_dead_cells(self):
        """
        Tworzy listę kluczy komórek które umrą w rundzie.
        """
        if len(self.__cells) > 0:
            for key, value in self.__cells.items():
                if value.model == None or not value.model.is_alive:
                    self.__keys_of_dead_cells.append(key)

    def __remove_dead_cells(self):
        """
        Usuwa wszystkie widoki martwych komórek, po kluczach komórek.
        """
        if len(self.__keys_of_dead_cells) > 0:
            for key in self.__keys_of_dead_cells:
                if self.__cells.get(key):
                    self.__cells.pop(key)

        self.__keys_of_dead_cells.clear()

    def __update_live_cells(self):
        """
        Aktualizuje pozycję widoków komórek.
        """
        if len(self.__cells):
            for rect in self.__cells.values():
                rect.update()

    def __print_all_live_cells(self):
        """
        Drukuje wszystkie widoki komórek.
        """
        if len(self.__cells):
            for rect in self.__cells.values():
                pygame.draw.ellipse(
                    self.__screen, self.COLOUR_CELLS, rect.body)

    def __print_text(self):
        """
        Drukuje wszystkie napisy w oknie.
        """
        # region lewy górny róg
        font = pygame.font.Font(self.FONT_NAME, self.FONT_SIZE)

        title_dead_cells = font.render(
            f'Umierających komórek: {self.__number_of_dead_cells}', True, self.COLOUR_TEXT)

        title_live_cells = font.render(
            f'Żywych komórek: {len(self.__cells)}', True,  self.COLOUR_TEXT)

        delay_info = font.render(
            f'Opóźnienie gry: {self.__current_game_delay}', True,  self.COLOUR_TEXT)

        number_of_rounds = font.render(
            f'Numer rundy: {self.__number_of_rounds}', True,  self.COLOUR_TEXT)

        self.__screen.blit(title_dead_cells, (15, 15))
        self.__screen.blit(title_live_cells, (15, 30))

        self.__screen.blit(delay_info, (15, 45))
        self.__screen.blit(number_of_rounds, (15, 60))
        # endregion
        # region lewy dolny róg
        information_about_pause_part_1 = font.render(
            f'Żeby zatrzymać grę należy wcisnąć SPACJĘ.', True,  self.COLOUR_TEXT, self.DARKRED)
        information_about_pause_part_2 = font.render(
            f'Żeby ją wznowić należy powtórnie wciśnąć SPCJĘ', True,  self.COLOUR_TEXT, self.DARKRED)
        information_about_delay_speed = font.render(
            f'Do przyspieszenia lub opóźnienia gry należy wciskać +/-', True,  self.COLOUR_TEXT, self.DARKRED)
        self.__screen.blit(information_about_delay_speed,
                           (15, self.WINDOW_HEIGHT-45))
        self.__screen.blit(information_about_pause_part_1,
                           (15, self.WINDOW_HEIGHT-30))
        self.__screen.blit(information_about_pause_part_2,
                           (15, self.WINDOW_HEIGHT-15))
        # endregion
        # region prawy dolny róg
        current_time_of_game = font.render(
            f'{datetime.datetime.now()-self.__start_time}', True,  self.COLOUR_TEXT)
        self.__screen.blit(current_time_of_game,
                           (self.WINDOW_WIDTH-100, self.WINDOW_HEIGHT-15))
        # endregion

    def start_game(self):
        """
        Inicjalizuje grę. 
        Zawarta tutaj jest główna pętla aplikacji.
        """
        pygame.init()
        pygame.display.set_caption(self.WINDOW_TITLE)

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
                            self.__print_text()

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

            self.__screen.fill(self.COLOUR_BACKGROUND)

            self.__delay_counter += 1

            if self.__delay_counter == self.__current_game_delay:
                self.__game.run()
                self.__make_list_of_dead_cells()
                # Przed usunięciem wszystkich martwych komórek żeby mieć dane nie używając niepotrzebnie dodatowych zmiennch.
                self.__number_of_dead_cells = len(self.__keys_of_dead_cells)
                self.__print_text()
                self.__remove_dead_cells()
                self.__add_new_cells()
                self.__update_live_cells()
                self.__delay_counter = 0
                self.__number_of_rounds += 1

            # Przed usunięciem wszystkich martwych komórek żeby mieć dane nie używając niepotrzebnie dodatowych zmiennch.
            self.__print_all_live_cells()
            self.__print_text()

            self.__clock.tick(self.REFRESH_RATE)
            pygame.display.flip()

        pygame.quit()
