from Models.game import Game
from Models.life_cell import LifeCell
from Models.location import Location
from Library.demonid import demonid
from Library.glider import glider
from Library.horizontal_line import horizontal_line
from Library.spaceship import spaceship
from Library.noah_ark import noah_ark


def main():
    game = Game(map_width=100, map_height=50)
    game.map_refresh_rate = 0.05
    game.number_of_cycles = 120
    game.is_stats_are_visibile = False
    demonid(game, 48, 10)
    demonid(game, 10, 10)
    glider(game, 0, 0)
    glider(game, 40, 0)

    glider(game, 0, 30)
    glider(game, 9, 30)

    horizontal_line(game, 10, 40)
    horizontal_line(game, 13, 40)
    horizontal_line(game, 16, 40)
    spaceship(game, 60, 20)
    noah_ark(game, 30, 15)
    game.run()


if __name__ == "__main__":
    main()
