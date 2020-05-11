from Views.cell_view import CellView
import pygame


class GameView:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    GRAY = (192, 192, 192)
    DARKRED = (139, 0, 0)
    MATRIX = (52, 195, 5)

    def __init__(self, model):
        self.__WINDOW_TITLE = "Life the game"
        self.__WINDOW_BACKGROUND_COLOUR = self.BLACK

        pygame.init()
        pygame.display.set_caption(self.__WINDOW_TITLE)

        self.__CELLS_WIDTH = 10
        self.__CELLS_HEIGHT = 10
        self.__CELLS_COLOUR = self.MATRIX

        self.__ROW_HEIGHT = 15
        self.__LEFT_MARGIN = 15
        self.__FONT_NAME = 'freesansbold.ttf'
        self.__FONT_SIZE = 12
        self.__FONT_COLOUR = self.WHITE
        self.__FONT = pygame.font.Font(self.__FONT_NAME, self.__FONT_SIZE)

        self.__model = model
        self.__window_width = self.__model.game_map.width * self.__CELLS_WIDTH
        self.__window_height = self.__model.game_map.height * self.__CELLS_HEIGHT
        self.__screen = pygame.display.set_mode(self.window_size)

        self.__text_print_top_left = []
        self.__text_print_bot_left = []

        self.__cells = {}
        self.__keys_of_dead_cells = []
        self.__number_of_dead_cells = 0

        self.__unchanging_text()

    @property
    def screen(self):
        return self.__screen

    @property
    def window_background(self):
        return self.__WINDOW_BACKGROUND_COLOUR

    @property
    def window_width(self):
        return self.__window_width

    @property
    def window_height(self):
        return self.__window_height

    @property
    def window_size(self):
        return (self.__window_width, self.__window_height)

    def __add_new_cells(self):
        """
        Dodaje wszystkie widoki komórek które są utworzone w instancji gry.
        """
        for key, value in self.__model.life_cells.items():
            if not self.__cells.get(key):
                new_cell = CellView(self.__screen, value)
                new_cell.width = self.__CELLS_WIDTH
                new_cell.height = self.__CELLS_HEIGHT
                new_cell.colour = self.__CELLS_COLOUR
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

    def print_all_live_cells(self):
        """
        Drukuje wszystkie widoki komórek.
        """
        if len(self.__cells):
            for rect in self.__cells.values():
                pygame.draw.ellipse(
                    self.__screen, self.__CELLS_COLOUR, rect.body)

    def __create_white_text(self, text: str):
        return self.__FONT.render(text, True, self.__FONT_COLOUR)

    def __create_white_text_red_background(self, text: str):
        return self.__FONT.render(text, True, self.__FONT_COLOUR, self.DARKRED)

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
        current_row_height = self.__window_height - self.__ROW_HEIGHT
        for text in self.__text_print_bot_left:
            self.__screen.blit(text, (self.__LEFT_MARGIN, current_row_height))
            current_row_height -= self.__ROW_HEIGHT

    def print_text(self):
        """
        Drukuje wszystkie napisy w oknie.
        """
        self.__print_text_top_left()
        self.__print_text_bot_left()

    def round(self):
        """
        Jeden przebieg rundy.
        """
        self.__make_list_of_dead_cells()
        self.__remove_dead_cells()
        self.__add_new_cells()
        self.__update_live_cells()
        self.print_text()
