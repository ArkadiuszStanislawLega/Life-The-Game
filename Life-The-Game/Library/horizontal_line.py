"""Autor: Arkadiusz Łęga, email:horemheb@vp.pl
Przechowuje koordynary reprezentujące określoną strukture złożoną z żywych komórek."""


def horizontal_line(game, coordinate_x: int, coordinate_y: int):
    """
    wysokość: 1
    szerokość: 3
    OOO
    Arguments:
        game {Game} -- Instancja gry do której ma zostać wstawiona struktura komórek.
        coordinate_x {int} -- Koordynat x od którego ma zostać tworzona struktura.
        coordinate_y {int} -- Koordynat x od którego ma zostać tworzona struktura.
    """
    coordinates = []
    coordinates.append((0, 0))
    coordinates.append((1, 0))
    coordinates.append((2, 0))

    game.put_coordinates_to_map(coordinates, coordinate_x, coordinate_y)
