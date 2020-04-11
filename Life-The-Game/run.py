from Models.game import Game
from Models.life_cell import LifeCell
from Models.location import Location


def main():
    game = Game(map_width=5, map_height=5)
    glider(game)
    game.run()


def glider(game):
    """
    Szybowiec
    """
    location = Location()
    location.X = 2
    location.Y = 0
    lifecell = LifeCell()
    lifecell.is_alive = True
    lifecell.location = location

    location2 = Location()
    location2.X = 3
    location2.Y = 1
    lifecell2 = LifeCell()
    lifecell2.is_alive = True
    lifecell2.location = location2

    location3 = Location()
    location3.X = 1
    location3.Y = 2
    lifecell3 = LifeCell()
    lifecell3.is_alive = True
    lifecell3.location = location3

    location4 = Location()
    location4.X = 2
    location4.Y = 2
    lifecell4 = LifeCell()
    lifecell4.is_alive = True
    lifecell4.location = location4

    location5 = Location()
    location5.X = 3
    location5.Y = 2
    lifecell5 = LifeCell()
    lifecell5.is_alive = True
    lifecell5.location = location5

    game.put_life_cell(lifecell)
    game.put_life_cell(lifecell2)
    game.put_life_cell(lifecell3)
    game.put_life_cell(lifecell4)
    game.put_life_cell(lifecell5)


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


def add_cells(game):
    location = Location()
    location.X = 2
    location.Y = 0
    lifecell = LifeCell()
    lifecell.is_alive = True
    lifecell.location = location

    location2 = Location()
    location2.X = 3
    location2.Y = 1
    lifecell2 = LifeCell()
    lifecell2.is_alive = True
    lifecell2.location = location2

    location3 = Location()
    location3.X = 1
    location3.Y = 2
    lifecell3 = LifeCell()
    lifecell3.is_alive = True
    lifecell3.location = location3

    location4 = Location()
    location4.X = 2
    location4.Y = 2
    lifecell4 = LifeCell()
    lifecell4.is_alive = True
    lifecell4.location = location4

    location5 = Location()
    location5.X = 3
    location5.Y = 2
    lifecell5 = LifeCell()
    lifecell5.is_alive = True
    lifecell5.location = location5

    # location6 = Location()
    # location6.X = 5
    # location6.Y = 4
    # lifecell6 = LifeCell()
    # lifecell6.is_alive = True
    # lifecell6.location = location6

    # location7 = Location()
    # location7.X = 3
    # location7.Y = 4
    # lifecell7 = LifeCell()
    # lifecell7.is_alive = True
    # lifecell7.location = location7

    # location8 = Location()
    # location8.X = 4
    # location8.Y = 4
    # lifecell8 = LifeCell()
    # lifecell8.is_alive = True
    # lifecell8.location = location8

    # location9 = Location()
    # location9.X = 4
    # location9.Y = 2
    # lifecell9 = LifeCell()
    # lifecell9.is_alive = True
    # lifecell9.location = location9

    game.put_life_cell(lifecell)
    game.put_life_cell(lifecell2)
    game.put_life_cell(lifecell3)
    game.put_life_cell(lifecell4)
    game.put_life_cell(lifecell5)
    # game.put_life_cell(lifecell6)
    # game.put_life_cell(lifecell7)
    # game.put_life_cell(lifecell8)
    # game.put_life_cell(lifecell9)


if __name__ == "__main__":
    main()
