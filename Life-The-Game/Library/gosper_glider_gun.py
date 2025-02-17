"""Autor: Arkadiusz Łęga, email:horemheb@vp.pl
Przechowuje koordynary reprezentujące określoną strukture złożoną z żywych komórek."""


def gosper_glider_gun(game, coordinate_x, coordinate_y):
    """
    wysokość: 9
    szerokość: 37

    Arguments:
        game {Game} -- Instancja gry do której ma zostać wstawiona struktura komórek.
        coordinate_x {int} -- Koordynat x od którego ma zostać tworzona struktura.
        coordinate_y {int} -- Koordynat x od którego ma zostać tworzona struktura.
    """

    coordinates = []
    coordinates.append((0, 4))
    coordinates.append((0, 5))

    coordinates.append((1, 4))
    coordinates.append((1, 5))

    coordinates.append((10, 4))
    coordinates.append((10, 5))
    coordinates.append((10, 6))

    coordinates.append((11, 3))
    coordinates.append((11, 7))

    coordinates.append((12, 2))
    coordinates.append((12, 8))

    coordinates.append((13, 2))
    coordinates.append((13, 8))

    coordinates.append((14, 5))

    coordinates.append((15, 3))
    coordinates.append((15, 7))

    coordinates.append((16, 4))
    coordinates.append((16, 5))
    coordinates.append((16, 6))

    coordinates.append((17, 5))

    coordinates.append((20, 2))
    coordinates.append((20, 3))
    coordinates.append((20, 4))

    coordinates.append((21, 2))
    coordinates.append((21, 3))
    coordinates.append((21, 4))

    coordinates.append((22, 1))
    coordinates.append((22, 5))

    coordinates.append((24, 0))
    coordinates.append((24, 1))
    coordinates.append((24, 5))
    coordinates.append((24, 6))

    coordinates.append((34, 2))
    coordinates.append((34, 3))

    coordinates.append((35, 2))
    coordinates.append((35, 3))

    game.put_coordinates_to_map(coordinates, coordinate_x, coordinate_y)
