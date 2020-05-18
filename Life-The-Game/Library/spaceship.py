"""Autor: Arkadiusz Łęga, email:horemheb@vp.pl
Przechowuje koordynary reprezentujące określoną strukture złożoną z żywych komórek."""


def spaceship(game, coordinate_x: int, coordinate_y: int):
    """
    wysokość: 18
    szerokość: 34
        .................................O.
        ................O...............O.O
        ......O.O......O.....OO........O...
        ......O....O....O.OOOOOO....OO.....
        ......O.OOOOOOOO..........O..O.OOO.
        .........O.....O.......OOOO....OOO.
        ....OO.................OOO.O.......
        .O..OO.......OO........OO..........
        .O..O..............................
        O..................................
        .O..O..............................
        .O..OO.......OO........OO..........
        ....OO.................OOO.O.......
        .........O.....O.......OOOO....OOO.
        ......O.OOOOOOOO..........O..O.OOO.
        ......O....O....O.OOOOOO....OO.....
        ......O.O......O.....OO........O...
        ................O...............O.O
        .................................O.
    Arguments:
        game {Game} -- Instancja gry do której ma zostać wstawiona struktura komórek.
        coordinate_x {int} -- Koordynat x od którego ma zostać tworzona struktura.
        coordinate_y {int} -- Koordynat x od którego ma zostać tworzona struktura.
    """

    coordinates = []
    coordinates.append((33, 0))

    coordinates.append((16, 1))
    coordinates.append((32, 1))
    coordinates.append((34, 1))

    coordinates.append((6, 2))
    coordinates.append((15, 2))
    coordinates.append((21, 2))
    coordinates.append((22, 2))
    coordinates.append((31, 2))

    coordinates.append((6, 3))
    coordinates.append((11, 3))
    coordinates.append((16, 3))
    coordinates.append((18, 3))
    coordinates.append((19, 3))
    coordinates.append((20, 3))
    coordinates.append((21, 3))
    coordinates.append((22, 3))
    coordinates.append((23, 3))
    coordinates.append((28, 3))
    coordinates.append((29, 3))

    coordinates.append((6, 4))
    coordinates.append((8, 4))
    coordinates.append((9, 4))
    coordinates.append((10, 4))
    coordinates.append((11, 4))
    coordinates.append((12, 4))
    coordinates.append((13, 4))
    coordinates.append((14, 4))
    coordinates.append((15, 4))
    coordinates.append((26, 4))
    coordinates.append((29, 4))
    coordinates.append((31, 4))
    coordinates.append((32, 4))
    coordinates.append((33, 4))

    coordinates.append((9, 5))
    coordinates.append((15, 5))
    coordinates.append((23, 5))
    coordinates.append((24, 5))
    coordinates.append((25, 5))
    coordinates.append((26, 5))
    coordinates.append((31, 5))
    coordinates.append((32, 5))
    coordinates.append((33, 5))

    coordinates.append((4, 6))
    coordinates.append((5, 6))
    coordinates.append((23, 6))
    coordinates.append((24, 6))
    coordinates.append((25, 6))
    coordinates.append((27, 6))

    coordinates.append((1, 7))
    coordinates.append((4, 7))
    coordinates.append((5, 7))
    coordinates.append((13, 7))
    coordinates.append((14, 7))
    coordinates.append((23, 7))
    coordinates.append((24, 7))

    coordinates.append((1, 8))
    coordinates.append((4, 8))

    coordinates.append((0, 9))

    coordinates.append((1, 10))
    coordinates.append((4, 10))

    coordinates.append((1, 11))
    coordinates.append((4, 11))
    coordinates.append((5, 11))
    coordinates.append((13, 11))
    coordinates.append((14, 11))
    coordinates.append((23, 11))
    coordinates.append((24, 11))

    coordinates.append((4, 12))
    coordinates.append((5, 12))
    coordinates.append((23, 12))
    coordinates.append((24, 12))
    coordinates.append((25, 12))
    coordinates.append((27, 12))

    coordinates.append((9, 13))
    coordinates.append((15, 13))
    coordinates.append((23, 13))
    coordinates.append((24, 13))
    coordinates.append((25, 13))
    coordinates.append((26, 13))
    coordinates.append((31, 13))
    coordinates.append((32, 13))
    coordinates.append((33, 13))

    coordinates.append((6, 14))
    coordinates.append((8, 14))
    coordinates.append((9, 14))
    coordinates.append((10, 14))
    coordinates.append((11, 14))
    coordinates.append((12, 14))
    coordinates.append((13, 14))
    coordinates.append((14, 14))
    coordinates.append((15, 14))
    coordinates.append((26, 14))
    coordinates.append((29, 14))
    coordinates.append((31, 14))
    coordinates.append((32, 14))
    coordinates.append((33, 14))

    coordinates.append((6, 15))
    coordinates.append((11, 15))
    coordinates.append((16, 15))
    coordinates.append((18, 15))
    coordinates.append((19, 15))
    coordinates.append((20, 15))
    coordinates.append((21, 15))
    coordinates.append((22, 15))
    coordinates.append((23, 15))
    coordinates.append((28, 15))
    coordinates.append((29, 15))

    coordinates.append((6, 16))
    coordinates.append((15, 16))
    coordinates.append((21, 16))
    coordinates.append((22, 16))
    coordinates.append((31, 16))

    coordinates.append((16, 17))
    coordinates.append((32, 17))
    coordinates.append((34, 17))

    coordinates.append((33, 18))

    game.put_coordinates_to_map(coordinates, coordinate_x, coordinate_y)
