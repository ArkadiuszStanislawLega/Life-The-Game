from Models.game import Game
from Models.life_cell import LifeCell
from Models.location import Location


def main():
    game = Game()

    add_cells(game)

    game.game_map.print_map()
    game.find_life_cells()


def add_cells(game):
    location = Location()
    location.X = 1
    location.Y = 1
    lifecell = LifeCell()
    lifecell.is_alive = True
    lifecell.location = location

    location2 = Location()
    location2.X = 2
    location2.Y = 0
    lifecell2 = LifeCell()
    lifecell2.is_alive = True
    lifecell2.location = location2

    location3 = Location()
    location3.X = 3
    location3.Y = 1
    lifecell3 = LifeCell()
    lifecell3.is_alive = True
    lifecell3.location = location3

    game.put_life_cell(lifecell)
    game.put_life_cell(lifecell2)
    game.put_life_cell(lifecell3)


if __name__ == "__main__":
    main()
