"""Autor: Arkadiusz Łęga, email:horemheb@vp.pl"""


class Location:
    """Klasa która przetrzymuje aktualną pozycje komórek na mapie.
    Kordynaty rosną od górnego lewego rogu w prawo i w dół.
    Lewy prawy róg przyjmuje wartość (0,0)
    """

    def __init__(self):
        """Ustawia koordynaty na 0"""
        self.__x = 0
        self.__y = 0

    @property
    def X(self):
        """Umożliwia dostęp do koordynatu x.

        Returns:
            [int] -- Koordynat x.
        """
        return self.__x

    @X.setter
    def X(self, value):
        """Umożliwia zmianę koordynatu x.

        Arguments:
            value {int} -- nowa wartość koordynatu x.
        """
        self.__x = value

    @property
    def Y(self):
        """Udostępnia wartośc koordynatu y.

        Returns:
            [int] -- koordynat y.
        """
        return self.__y

    @Y.setter
    def Y(self, value):
        """Umożliwia zmianę koordynatu y.

        Arguments:
            value {int} -- nowa wartość koordynatu y.
        """
        self.__y = value

    def __str__(self):
        return f'({self.__x}, {self.__y})'
