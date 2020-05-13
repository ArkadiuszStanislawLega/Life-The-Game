from Views.view import View
from Views.info_life_cells_view import InfoLifeCellsView
from Library.colours import colours
import pygame


class TextView(View):
    """ Klasa jest odpowiedzialna za wyświetlanie napisów w czasie trwania rozgrywki."""

    def __init__(self, model, screen):
        super().__init__(name="TextView", model=model)
        self.__screen = screen
        self.__ROW_HEIGHT = 15
        self.__LEFT_MARGIN = 15
        self.__FONT_NAME = 'freesansbold.ttf'
        self.__FONT_SIZE = 12
        self.__FONT_COLOUR = colours.WHITE
        self.__FONT = pygame.font.Font(self.__FONT_NAME, self.__FONT_SIZE)

        self.__text_print_top_left = []
        self.__text_print_bot_left = []

        self.__unchanging_text()

        self.__info_life_cells_view = InfoLifeCellsView(
            screen=self.__screen, model=self._model.life_cells)

        self.add_component(self.__info_life_cells_view)

    @property
    def info_life_cells_view(self):
        return self.__info_life_cells_view

    def __create_white_text(self, text: str):
        """
        Tworzy widok napisu którego czcionka jest biała i nie posiada tła.

        Arguments:
            text {str} -- Napis do wyświetlenia.

        Returns:
            [pygame.font.Font] -- Napis o standardowej czcionce w kolorze białym bez tła.
        """
        return self.__FONT.render(text, True, self.__FONT_COLOUR)

    def __create_white_text_red_background(self, text: str):
        """
        Tworzy widok napisu którego czcionka jest biała a tło ciemno czerwone.

        Arguments:
            text {str} -- Napis do wyświetlenia.

        Returns:
            [pygame.font.Font] -- Napis o standardowej czcionce w kolorze białym na ciemno czerwonym tle.
        """
        return self.__FONT.render(text, True, self.__FONT_COLOUR, colours.DARK_RED)

    def add_text_top_left(self, text: str):
        """
        Dodaje kolejny wiersz do "grida" wyświetlającego napisy
        w górnym lewym rogu planszy.

        Arguments:
            text {str} -- Napis który ma zostać dodany.
        """
        if isinstance(text, str):
            self.__text_print_top_left.append(
                self.__create_white_text(text))

    def add_text_bot_left(self, text: str):
        """
        Dodaje kolejny wiersz do "grida" wyświetlającego napisy
        w dolnym lewym rogu planszy.

        Arguments:
            text {str} -- Napis który ma zostać dodany.
        """
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
            f'Żeby ją wznowić należy powtórnie wciśnąć SPACJĘ')
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
        width, height = pygame.display.get_surface().get_size()
        current_row_height = height - self.__ROW_HEIGHT
        for text in self.__text_print_bot_left:
            self.__screen.blit(text, (self.__LEFT_MARGIN, current_row_height))
            current_row_height -= self.__ROW_HEIGHT

    def __print_backround(self):
        """
        Drukuje tło w górnej lewej części ekranu po wszystkimi napisamy.
        Celem jest odświerzanie widoków napisów.
        """
        width = 170
        height = len(self.__text_print_top_left) * self.__ROW_HEIGHT + 15

        distance_from_the_top = 10
        distance_from_the_left = 10
        coordinates = (distance_from_the_left // 1, distance_from_the_top // 1)

        size = (width, height)

        position = (coordinates, size)

        pygame.draw.rect(self.__screen, colours.BLACK, position, 0)

    def print_text(self):
        """
        Drukuje wszystkie napisy w oknie.
        """
        self.__print_backround()
        self.__print_text_top_left()
        self.__print_text_bot_left()

    def add_component(self, comp):
        if comp.name not in self._component_list:
            self._component_list[comp.name] = comp

    def update(self, *args, **kwargs):
        pass

    def show(self):
        pass
