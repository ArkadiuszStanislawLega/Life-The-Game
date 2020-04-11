from Models.game import Game
from Models.life_cell import LifeCell
from Models.location import Location
from Library.demonid import demonid
from Library.glider import glider
from Library.horizontal_line import horizontal_line
from Library.spaceship import spaceship


def main():
    game = Game(map_width=60, map_height=60)
    game.map_refresh_rate = 0.02
    game.number_of_cycles = 120
    game.is_stats_are_visibile = False
    #demonid(game, 28, 10)
    #demonid(game, 10, 10)
    glider(game, 0, 0)
    glider(game, 20, 0)
    #horizontal_line(game, 10, 40)
    #horizontal_line(game, 13, 40)
    #horizontal_line(game, 16, 40)
    spaceship(game, 20, 20)
    game.run()


def line(game):
    """
    Prosta linia
    """
    location = Location()
    location.X = 0
    location.Y = 1
    lifecell = LifeCell()
    lifecell.is_alive = True
    lifecell.location = location

    location2 = Location()
    location2.X = 1
    location2.Y = 1
    lifecell2 = LifeCell()
    lifecell2.is_alive = True
    lifecell2.location = location2

    location3 = Location()
    location3.X = 2
    location3.Y = 1
    lifecell3 = LifeCell()
    lifecell3.is_alive = True
    lifecell3.location = location3

    game.put_life_cell(lifecell)
    game.put_life_cell(lifecell2)
    game.put_life_cell(lifecell3)


if __name__ == "__main__":
    main()
