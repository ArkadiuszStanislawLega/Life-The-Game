from Views.view import View
from Library.colours import colours
import pygame


class TextView(View):
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
        current_row_height = self._model.window_height - self.__ROW_HEIGHT
        for text in self.__text_print_bot_left:
            self.__screen.blit(text, (self.__LEFT_MARGIN, current_row_height))
            current_row_height -= self.__ROW_HEIGHT

    def __print_backround(self):
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
