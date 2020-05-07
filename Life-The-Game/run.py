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

WIDTH = 700
HEIGHT = 500

SIZE = (WIDTH, HEIGHT)

WINDOW_TITLE = "Life the game"


def main():
    pygame.init()

    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    carry_on = True

    clock = pygame.time.Clock()
    counter = 0

    cell = CellView(screen)
    while carry_on:

        # --- Main event loop
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                carry_on = False             # Flag that we are done so we exit this loop

        # --- Game logic should go here

        # --- Drawing code should go here
        # First, clear the screen to white.
        screen.fill(COLOUR_BACKGROUND)

        new_left_position = cell.distance_from_the_left + 10
        new_top_position = cell.distance_from_the_top + 10

        font = pygame.font.Font('freesansbold.ttf', 10)
        text = font.render(f'{new_left_position}', True, GREEN, RED)
        textRect = text.get_rect()
        textRect.center = (200 // 2, 200 // 2)

        screen.blit(text, textRect)
        screen.blit(screen,
                    (new_left_position, new_top_position),  cell.body)

        cell.change_location(new_left_position, new_top_position)

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        counter += 1
        clock.tick(60)

    # Once we have exited the main program loop we can stop the game engine:
    pygame.quit()


if __name__ == "__main__":
    main()
