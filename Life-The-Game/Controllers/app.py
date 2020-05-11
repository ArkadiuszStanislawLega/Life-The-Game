from Models.game import Game
from Models.life_cell import LifeCell
from Models.location import Location
from Library.demonid import demonid
from Library.glider import glider
from Library.horizontal_line import horizontal_line
from Library.spaceship import spaceship
from Library.noah_ark import noah_ark
from Library.info import struct_info
from Library.gosper_glider_gun import gosper_glider_gun
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
    LEFT_MARGIN = 15

    GAME_WIDTH = 120
    GAME_HEIGHT = 60

    CELLS_WIDTH = 10
    CELLS_HEIGHT = 10

    WINDOW_WIDTH = GAME_WIDTH*CELLS_WIDTH
    WINDOW_HEIGHT = GAME_HEIGHT*CELLS_HEIGHT

    WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
    WINDOW_TITLE = "Life the game"

    def __init__(self):
        self.__struct = {"glider": glider,
                         "spaceship": spaceship,
                         "noah_ark": noah_ark,
                         "demonid": demonid,
                         "gosper_glider_gun": gosper_glider_gun}
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

    def generate_stuct_in_random_loc(self, name):
        info = struct_info().get(name)
        self.__struct.get(name)(self.__game, self.gen_random_x(
            info), self.gen_random_y(info))

    def try_generate_struct(self, name: str, max_number_of_struct: int, min_number_of_struct: int, max_chance_to_generate: int):
        chance = random.randrange(
            0, max_chance_to_generate)
        if chance < 1000:
            number_of_struct = random.randrange(
                min_number_of_struct, max_number_of_struct)
            for i in range(number_of_struct):
                self.generate_stuct_in_random_loc(name)

    def __cells_at_the_begginning(self):
        """
        Początkowy układ komórek przy uruchomieniu aplikacji.
        """
        # self.try_generate_struct(name="demonid",
        #                          min_number_of_struct=1,
        #                          max_number_of_struct=4,
        #                          max_chance_to_generate=2000)

        # self.try_generate_struct(name="spaceship",
        #                          min_number_of_struct=1,
        #                          max_number_of_struct=2,
        #                          max_chance_to_generate=3000)

        # self.try_generate_struct(name="glider",
        #                          min_number_of_struct=1,
        #                          max_number_of_struct=8,
        #                          max_chance_to_generate=1500)

        # self.try_generate_struct(name="noah_ark",
        #                          min_number_of_struct=1,
        #                          max_number_of_struct=2,
        #                          max_chance_to_generate=3000)

        self.try_generate_struct(name="gosper_glider_gun",
                                 min_number_of_struct=1,
                                 max_number_of_struct=2,
                                 max_chance_to_generate=1000)

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

        self.__screen.blit(title_dead_cells, (self.LEFT_MARGIN, 15))
        self.__screen.blit(title_live_cells, (self.LEFT_MARGIN, 30))

        self.__screen.blit(delay_info, (self.LEFT_MARGIN, 45))
        self.__screen.blit(number_of_rounds, (self.LEFT_MARGIN, 60))
        # endregion
        # region lewy dolny róg
        information_about_pause_part_1 = font.render(
            f'Żeby zatrzymać grę należy wcisnąć SPACJĘ.', True,  self.COLOUR_TEXT, self.DARKRED)
        information_about_pause_part_2 = font.render(
            f'Żeby ją wznowić należy powtórnie wciśnąć SPCJĘ', True,  self.COLOUR_TEXT, self.DARKRED)
        information_about_delay_speed = font.render(
            f'Do przyspieszenia lub opóźnienia gry należy wciskać +/-', True,  self.COLOUR_TEXT, self.DARKRED)
        self.__screen.blit(information_about_delay_speed,
                           (self.LEFT_MARGIN, self.WINDOW_HEIGHT-45))
        self.__screen.blit(information_about_pause_part_1,
                           (self.LEFT_MARGIN, self.WINDOW_HEIGHT-30))
        self.__screen.blit(information_about_pause_part_2,
                           (self.LEFT_MARGIN, self.WINDOW_HEIGHT-15))
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
