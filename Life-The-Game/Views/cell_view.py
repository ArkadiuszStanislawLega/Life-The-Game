import pygame


class CellView:
    LIVE_COLOUR = (139, 0, 0)
    DEAD_COLOUR = (0, 0, 0)

    HEIGHT = 10
    WIDTH = 10

    def __init__(self, screen):
        self.__distance_from_the_top = 10
        self.__distance_from_the_left = 10
        self.__width = self.WIDTH
        self.__height = self.HEIGHT
        self.__screen = screen
        self.__position = [self.__distance_from_the_left,
                           self.__distance_from_the_top, self.__width, self.__height]

        self.__body = pygame.draw.ellipse(
            self.__screen, self.LIVE_COLOUR, self.__position, 0)

        self.__screen_surface = pygame.display.get_surface().get_size()
        self.__right_border = self.__screen_surface[0]
        self.__bot_border = self.__screen_surface[1]

    @property
    def body(self):
        return self.__body

    @property
    def distance_from_the_top(self):
        return self.__distance_from_the_top

    @property
    def distance_from_the_left(self):
        return self.__distance_from_the_left

    def change_location(self, top, left):
        if isinstance(top, int) and isinstance(left, int):
            if top > 0 and left > 0:
                if top < self.__bot_border - self.__height and left < self.__right_border - self.__width:
                    self.__distance_from_the_top = top
                    self.__distance_from_the_lef = left
