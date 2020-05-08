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
    pygame.init()

    game = Game(map_width=120, map_height=80)
    game.map_refresh_rate = 0.05
    game.number_of_cycles = 120
    game.is_stats_are_visibile = False

    horizontal_line(game, 10, 10)
    demonid(game, 40, 20)
    spaceship(game, 50, 40)

    game.run()

    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    carry_on = True

    clock = pygame.time.Clock()

    counter = 0

    cells = {}

    while carry_on:

        # --- Main event loop
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                carry_on = False             # Flag that we are done so we exit this loop

        # --- Game logic should go here

        screen.fill(COLOUR_BACKGROUND)

        counter += 1

        if counter == 10:
            game.run()

            for key, value in game.life_cells.items():
                if not cells.get(key):
                    cells.update({key: CellView(screen, value)})

            dead_cells_key = []

            for key, value in cells.items():
                if value.model == None or not value.model.is_alive:
                    dead_cells_key.append(key)

            for key in dead_cells_key:
                if cells.get(key):
                    cells.pop(key)

            for rect in cells.values():
                rect.update()

            counter = 0

            # pygame.draw.ellipse(screen, BLACK, cell.body)
        for rect in cells.values():
            pygame.draw.ellipse(screen, BLACK, rect.body)

        clock.tick(60)
        pygame.display.flip()

    # Once we have exited the main program loop we can stop the game engine:
    pygame.quit()


if __name__ == "__main__":
    main()
