from Models.game import Game
from Models.life_cell import LifeCell
from Models.location import Location
from Library.demonid import demonid
from Library.glider import glider
from Library.horizontal_line import horizontal_line
from Library.spaceship import spaceship
from Library.noah_ark import noah_ark
from Views.cell_view import CellView
import pygame


class App():
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    GRAY = (192, 192, 192)
    DARKRED = (139, 0, 0)

    COLOUR_BACKGROUND = GRAY

    GAME_WIDTH = 120
    GAME_HEIGHT = 80

    REFRESH_RATE = 60

    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 800

    WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
    WINDOW_TITLE = "Life the game"

    def __init__(self):
        self.__cells = {}
        self.__keys_of_dead_cells = []
        self.__screen = pygame.display.set_mode(self.WINDOW_SIZE)
        self.__clock = pygame.time.Clock()
        self.__game_delay = 1
        self.__delay_counter = 0
        self.__is_working = True

        self.__game = Game(map_width=self.GAME_WIDTH,
                           map_height=self.GAME_HEIGHT)
        self.__game.is_stats_are_visibile = False

        self.cells_at_the_begginning()

        self.start_game()

    def cells_at_the_begginning(self):
        horizontal_line(self.__game, 10, 10)
        demonid(self.__game, 40, 20)
        spaceship(self.__game, 30, 60)

        glider(self.__game, 80, 10)
        glider(self.__game, 90, 10)
        glider(self.__game, 100, 10)
        glider(self.__game, 110, 10)

        noah_ark(self.__game, 80, 20)

    def add_new_cells(self):
        for key, value in self.__game.life_cells.items():
            if not self.__cells.get(key):
                self.__cells.update({key: CellView(self.__screen, value)})

    def make_list_of_dead_cells(self):
        if len(self.__cells) > 0:
            for key, value in self.__cells.items():
                if value.model == None or not value.model.is_alive:
                    self.__keys_of_dead_cells.append(key)

    def remove_dead_cells(self):
        if len(self.__keys_of_dead_cells) > 0:
            for key in self.__keys_of_dead_cells:
                if self.__cells.get(key):
                    self.__cells.pop(key)

        self.__keys_of_dead_cells.clear()

    def update_live_cells(self):
        if len(self.__cells):
            for rect in self.__cells.values():
                rect.update()

    def print_all_live_cells(self):
        if len(self.__cells):
            for rect in self.__cells.values():
                pygame.draw.ellipse(self.__screen, self.BLACK, rect.body)

    def print_text(self):
        font = pygame.font.Font('freesansbold.ttf', 12)

        text = font.render(
            f'Umiera: {len(self.__keys_of_dead_cells)} komórek', True, self.DARKRED, self.GRAY)
        textRect = text.get_rect()
        textRect.center = (100 // 1, 10 // 1)

        text2 = font.render(
            f'Żywych komórek: {len(self.__cells)}', True,  self.DARKRED, self.GRAY)
        textRect2 = text2.get_rect()
        textRect2.center = (100 // 1, 25 // 1)

        self.__screen.blit(text, textRect)
        self.__screen.blit(text2, textRect2)

    def start_game(self):
        pygame.init()
        pygame.display.set_caption(self.WINDOW_TITLE)

        while self.__is_working:

            # --- Main event loop
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    self.__is_working = False             # Flag that we are done so we exit this loop

            # --- Game logic should go here

            self.__screen.fill(self.COLOUR_BACKGROUND)

            self.__delay_counter += 1

            if self.__delay_counter == self.__game_delay:
                self.__game.run()
                self.make_list_of_dead_cells()
                self.print_text()
                self.remove_dead_cells()
                self.add_new_cells()
                self.update_live_cells()
                self.__delay_counter = 0

            self.print_all_live_cells()

            self.__clock.tick(self.REFRESH_RATE)
            pygame.display.flip()

        # Once we have exited the main program loop we can stop the game engine:
        pygame.quit()
