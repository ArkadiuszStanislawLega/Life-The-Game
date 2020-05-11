def horizontal_line(game, x, y):
    """
    wysokość: 1
    szerokość: 3
    OOO
    """
    coordinates = []
    coordinates.append((0, 0))
    coordinates.append((1, 0))
    coordinates.append((2, 0))

    game.put_coordinates_to_map(coordinates, x, y)
