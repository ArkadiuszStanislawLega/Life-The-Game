from Models.game import Game


def glider(game: Game, x, y):
    """
    wysokość: 3
    szerokość: 3
     O
      O
    OOO
    """
    coordinates = []
    coordinates.append((1, 0))

    coordinates.append((2, 1))

    coordinates.append((0, 2))
    coordinates.append((1, 2))
    coordinates.append((2, 2))

    game.put_coordinates_to_map(coordinates, x, y)
