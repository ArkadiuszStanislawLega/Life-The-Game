import pygame


class CellView:
    LIVE_COLOUR = (139, 0, 0)
    DEAD_COLOUR = (0, 0, 0)

    HEIGHT = 10
    WIDTH = 10

    MARGIN = 2

    def __init__(self, screen, model):
        self.__distance_from_the_top = 10
        self.__distance_from_the_left = 10
        self.__coordinates = (self.__distance_from_the_left // 2,
                              self.__distance_from_the_top // 2)

        self.__width = self.WIDTH
        self.__height = self.HEIGHT
        self.__size = (self.__width, self.__height)
        self.__screen = screen

        self.__position = (self.__coordinates, self.__size)

        self.__body = pygame.draw.ellipse(
            self.__screen, self.LIVE_COLOUR, self.__position, 0)

        self.__screen_surface = pygame.display.get_surface().get_size()
        self.__right_border = self.__screen_surface[0]
        self.__bot_border = self.__screen_surface[1]
        self.__model = model

    @property
    def model(self):
        return self.__model

    @property
    def name(self):
        return self.__model.name

    @property
    def body(self):
        return self.__body

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def distance_from_the_top(self):
        return self.__distance_from_the_top

    @property
    def distance_from_the_left(self):
        return self.__distance_from_the_left

    @property
    def position(self):
        return self.__position

    def update(self):
        self.__distance_from_the_top = self.__model.location.X * self.__width
        self.__distance_from_the_left = self.__model.location.Y * self.__height

        self.__coordinates = (self.__distance_from_the_top // 1,
                              self.__distance_from_the_left // 1)

        self.__position = (self.__coordinates, self.__size)

        self.__body = pygame.draw.ellipse(
            self.__screen, self.LIVE_COLOUR, self.__position, 0)
