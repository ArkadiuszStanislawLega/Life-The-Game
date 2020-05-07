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

    cells = [CellView(screen), CellView(screen), CellView(screen)]

    cells[0].change_coordinates(10, 20)
    cells[1].change_coordinates(10, 30)
    cells[2].change_coordinates(10, 40)

    cell = CellView(screen)
    while carry_on:

        # --- Main event loop
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                carry_on = False             # Flag that we are done so we exit this loop

        # --- Game logic should go here

        screen.fill(COLOUR_BACKGROUND)

        new_left_position = cell.distance_from_the_left + 1
        new_top_position = cell.distance_from_the_top + 1

        font = pygame.font.Font('freesansbold.ttf', 10)
        text = font.render(f'{new_left_position}', True, GREEN, BLACK)
        textRect = text.get_rect()
        textRect.center = (200 // 2, 200 // 2)

        screen.blit(text, textRect)

        cell.change_coordinates(new_left_position, new_top_position)

        if counter == 50:
            cells.remove(cells[2])
        if counter == 100:
            cells.remove(cells[1])
        if counter == 150:
            cells.remove(cells[0])

        for rect in cells:
            pygame.draw.ellipse(screen, BLACK, rect.body)

        pygame.draw.ellipse(screen, BLACK, cell.body)

        counter += 1
        clock.tick(60)
        pygame.display.flip()

    # Once we have exited the main program loop we can stop the game engine:
    pygame.quit()


if __name__ == "__main__":
    main()
