from Models.game import Game
from Models.life_cell import LifeCell
from Models.location import Location
from Library.demonid import demonid
from Library.glider import glider
from Library.horizontal_line import horizontal_line
from Library.spaceship import spaceship
from Library.noah_ark import noah_ark
from Views.cell_view import CellView
from Controllers.app import App
import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (192, 192, 192)
DARKRED = (139, 0, 0)

COLOUR_BACKGROUND = GRAY

WIDTH = 1200
HEIGHT = 800

SIZE = (WIDTH, HEIGHT)

WINDOW_TITLE = "Life the game"


def main():
    App()


if __name__ == "__main__":
    main()
