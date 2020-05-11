from Models.game import Game


def demonid(game: Game, x, y):
    """
    wysokość: 18
    szerokość: 12

            OO      OO
           O O      O O
           O          O
        OO O          O OO
        OO O O  OO  O O OO
           O O O  O O O
           O O O  O O O
        OO O O  OO  O O OO
        OO O          O OO
           O          O
           O O      O O
            OO      OO
    """
    coordinates = []
    coordinates.append((4, 0))
    coordinates.append((5, 0))
    coordinates.append((12, 0))
    coordinates.append((13, 0))

    coordinates.append((3, 1))
    coordinates.append((5, 1))
    coordinates.append((12, 1))
    coordinates.append((14, 1))

    coordinates.append((3, 2))
    coordinates.append((14, 2))

    coordinates.append((0, 3))
    coordinates.append((1, 3))
    coordinates.append((3, 3))
    coordinates.append((14, 3))
    coordinates.append((16, 3))
    coordinates.append((17, 3))

    coordinates.append((0, 4))
    coordinates.append((1, 4))
    coordinates.append((3, 4))
    coordinates.append((5, 4))
    coordinates.append((8, 4))
    coordinates.append((9, 4))
    coordinates.append((12, 4))
    coordinates.append((14, 4))
    coordinates.append((16, 4))
    coordinates.append((17, 4))

    coordinates.append((3, 5))
    coordinates.append((5, 5))
    coordinates.append((7, 5))
    coordinates.append((10, 5))
    coordinates.append((12, 5))
    coordinates.append((14, 5))

    coordinates.append((3, 6))
    coordinates.append((5, 6))
    coordinates.append((7, 6))
    coordinates.append((10, 6))
    coordinates.append((12, 6))
    coordinates.append((14, 6))

    coordinates.append((0, 7))
    coordinates.append((1, 7))
    coordinates.append((3, 7))
    coordinates.append((5, 7))
    coordinates.append((8, 7))
    coordinates.append((9, 7))
    coordinates.append((12, 7))
    coordinates.append((14, 7))
    coordinates.append((16, 7))
    coordinates.append((17, 7))

    coordinates.append((0, 8))
    coordinates.append((1, 8))
    coordinates.append((3, 8))
    coordinates.append((14, 8))
    coordinates.append((16, 8))
    coordinates.append((17, 8))

    coordinates.append((3, 9))
    coordinates.append((14, 9))

    coordinates.append((3, 10))
    coordinates.append((5, 10))
    coordinates.append((12, 10))
    coordinates.append((14, 10))

    coordinates.append((4, 11))
    coordinates.append((5, 11))
    coordinates.append((12, 11))
    coordinates.append((13, 11))

    game.put_coordinates_to_map(coordinates, x, y)
