"""Autor: Arkadiusz Łęga, email:horemheb@vp.pl
Przechowuje koordynary reprezentujące określoną strukture złożoną z żywych komórek."""


def glider(game, coordinate_x, coordinate_y):
    """
    wysokość: 3
    szerokość: 3
     O
      O
    OOO

    Arguments:
        game {Game} -- Instancja gry do której ma zostać wstawiona struktura komórek.
        coordinate_x {int} -- Koordynat x od którego ma zostać tworzona struktura.
        coordinate_y {int} -- Koordynat x od którego ma zostać tworzona struktura.
    """
    coordinates = []
    coordinates.append((1, 0))

    coordinates.append((2, 1))

    coordinates.append((0, 2))
    coordinates.append((1, 2))
    coordinates.append((2, 2))

    game.put_coordinates_to_map(coordinates, coordinate_x, coordinate_y)
