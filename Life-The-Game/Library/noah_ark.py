"""Autor: Arkadiusz Łęga, email:horemheb@vp.pl
Przechowuje koordynary reprezentujące określoną strukture złożoną z żywych komórek."""


def noah_ark(game,  coordinate_x: int, coordinate_y: int):
    """
    wysokość: 14
    szerokość: 14
            O O
           O
            O  O
              OOO




     O
    O O

    O  O
      OO
       O

    Arguments:
        game {Game} -- Instancja gry do której ma zostać wstawiona struktura komórek.
        coordinate_x {int} -- Koordynat x od którego ma zostać tworzona struktura.
        coordinate_y {int} -- Koordynat x od którego ma zostać tworzona struktura.
    """
    coordinates = []
    coordinates.append((10, 0))
    coordinates.append((12, 0))

    coordinates.append((9, 1))

    coordinates.append((10, 2))
    coordinates.append((13, 2))

    coordinates.append((12, 3))
    coordinates.append((13, 3))
    coordinates.append((14, 3))

    coordinates.append((1, 9))

    coordinates.append((0, 10))
    coordinates.append((2, 10))

    coordinates.append((0, 12))
    coordinates.append((3, 12))

    coordinates.append((2, 13))
    coordinates.append((3, 13))

    coordinates.append((3, 14))

    game.put_coordinates_to_map(coordinates,  coordinate_x, coordinate_y)
