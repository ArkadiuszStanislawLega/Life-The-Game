import pygame
from Views.map_cell_view import MapCellView
from Views.view import View
from Views.map_view import MapView
from Views.life_cell_view import LifeCellView
from Library.colours import colours


class GameView(View):

    def __init__(self, model):
        super().__init__(name="GameView", model=model)
        self.__WINDOW_TITLE = "Life the game"
        self.__WINDOW_BACKGROUND_COLOUR = colours.BLACK

        pygame.init()
        pygame.display.set_caption(self.__WINDOW_TITLE)

        self.__CELLS_WIDTH = 10
        self.__CELLS_HEIGHT = 10
        self.__CELLS_COLOUR = colours.MATRIX

        self.__ROW_HEIGHT = 15
        self.__LEFT_MARGIN = 15
        self.__FONT_NAME = 'freesansbold.ttf'
        self.__FONT_SIZE = 12
        self.__FONT_COLOUR = colours.WHITE
        self.__FONT = pygame.font.Font(self.__FONT_NAME, self.__FONT_SIZE)

        self.__window_width = self._model.game_map.width * self.__CELLS_WIDTH
        self.__window_height = self._model.game_map.height * self.__CELLS_HEIGHT
        self.__screen = pygame.display.set_mode(self.window_size)

        self.__text_print_top_left = []
        self.__text_print_bot_left = []

        self.__map_view = MapView(
            model=self._model.game_map, screen=self.__screen)
        self.add_component(self.__map_view)

        self._model.game_map.add_observer(self.__map_view)

        self.__map_cell_views = {}
        self.__life_cell_views = {}
        self.__number_of_dead_cells = 0
        self.__dead_life_cells_keys = []
        self.__add_new_cells()
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
        for key, value in self._model.life_cells.items():
            if not self.__map_cell_views.get(key):
                new_cell = MapCellView(screen=self.__screen, model=value)
                new_cell.width = self.__CELLS_WIDTH
                new_cell.height = self.__CELLS_HEIGHT
                new_cell.colour = self.__CELLS_COLOUR
                self.__map_cell_views.update({key: new_cell})

    def __make_list_of_dead_cells(self):
        """
        Tworzy listę kluczy komórek które umrą w rundzie.
        """
        self.__number_of_dead_cells += 0
        if len(self.__life_cell_views) > 0:
            for key, value in self.__life_cell_views.items():
                if not value.model.is_alive:
                    self.__life_cell_views.get(key).update()
                    self.__number_of_dead_cells += 1
                    self.__dead_life_cells_keys.append(key)

            for key in self.__dead_life_cells_keys:
                self.__life_cell_views.pop(key)

            self.__dead_life_cells_keys.clear()

    def __update_live_cells(self):
        """
        Aktualizuje pozycję widoków komórek.
        """
        if len(self.__life_cell_views):
            for map_cell_view in self.__life_cell_views.values():
                map_cell_view.update()

    def print_all_live_cells(self):
        """
        Drukuje wszystkie widoki komórek.
        """
        if len(self.__life_cell_views):
            for view in self.__life_cell_views.values():
                view.body

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
        self.__update_live_cells()
        self.print_all_live_cells()
        self.print_text()

    def add_component(self, comp):
        if comp.name not in self._component_list:
            self._component_list[comp.name] = comp

    def update(self, *args, **kwargs):
        if len(kwargs) > 0:
            key = kwargs.get("key")
            value = kwargs.get("value")

            if key == "NewLifeCell":
                if not self._component_list.get(f'LifeCellView:{value.name}'):
                    view = LifeCellView(screen=self.__screen, model=value)
                    view.name += f':{value.location}'
                    value.add_observer(view)
                    self.__life_cell_views[view.name] = view
                    self.__map_view.update(key=key, value=view)

    def show(self):
        self.__map_view.show()

        for life_cell in self.__life_cell_views.values():
            life_cell.show()
