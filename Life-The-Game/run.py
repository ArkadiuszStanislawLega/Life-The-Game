from Models.game import Game
from Models.life_cell import LifeCell
from Models.location import Location


def main():
    game = Game()

    lifecell = LifeCell()
    location = Location()
    location.X = 5
    location.Y = 5

    lifecell.is_life = True
    lifecell.location = location

    lifecell2 = LifeCell()
    location2 = Location()
    location2.X = 3
    location2.Y = 3

    lifecell2.is_life = False
    lifecell2.location = location2

    game.put_life_cell(lifecell)
    game.put_life_cell(lifecell2)

    game.game_map.print_map()


if __name__ == "__main__":
    main()
