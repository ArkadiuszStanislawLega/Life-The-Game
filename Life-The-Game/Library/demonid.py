from Models.game import Game


def demonid(game: Game, x, y):
    """
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
    coordinates.append((0, 4))
    coordinates.append((0, 5))
    coordinates.append((0, 12))
    coordinates.append((0, 13))

    coordinates.append((1, 3))
    coordinates.append((1, 5))
    coordinates.append((1, 12))
    coordinates.append((1, 14))

    coordinates.append((2, 3))
    coordinates.append((2, 14))

    coordinates.append((3, 0))
    coordinates.append((3, 1))
    coordinates.append((3, 3))
    coordinates.append((3, 14))
    coordinates.append((3, 16))
    coordinates.append((3, 17))

    coordinates.append((4, 0))
    coordinates.append((4, 1))
    coordinates.append((4, 3))
    coordinates.append((4, 8))
    coordinates.append((4, 9))
    coordinates.append((4, 14))
    coordinates.append((4, 16))
    coordinates.append((4, 17))

    coordinates.append((5, 3))
    coordinates.append((5, 5))
    coordinates.append((5, 6))
    coordinates.append((5, 10))
    coordinates.append((5, 12))

    coordinates.append((6, 3))
    coordinates.append((6, 5))
    coordinates.append((6, 6))
    coordinates.append((6, 10))
    coordinates.append((6, 12))

    coordinates.append((7, 0))
    coordinates.append((7, 1))
    coordinates.append((7, 3))
    coordinates.append((7, 4))
    coordinates.append((7, 8))
    coordinates.append((7, 9))
    coordinates.append((7, 12))
    coordinates.append((7, 14))
    coordinates.append((7, 16))
    coordinates.append((7, 17))

    coordinates.append((8, 0))
    coordinates.append((8, 1))
    coordinates.append((8, 3))
    coordinates.append((8, 14))
    coordinates.append((8, 16))
    coordinates.append((8, 17))

    coordinates.append((9, 3))
    coordinates.append((9, 14))

    coordinates.append((10, 3))
    coordinates.append((10, 4))
    coordinates.append((10, 12))
    coordinates.append((10, 14))

    coordinates.append((11, 4))
    coordinates.append((11, 5))
    coordinates.append((11, 12))
    coordinates.append((11, 13))

    game.put_coordinates_to_map(coordinates, x, y)
