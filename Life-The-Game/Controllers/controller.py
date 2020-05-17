from abc import ABC, abstractmethod


class Controller(ABC):
    """Abstrakcyjna klasa kontrolera."""

    def __init__(self, model=None, view=None):
        """
        Podstawowy kontruktor klasy. Przypisuje model i widok do właściwości klasy.

        Arguments:
            ABC {[type]} -- [description]

        Keyword Arguments:
            model {[type]} -- Instancja klasy z której będą pobierane dane. (default: {None})
            view {[type]} -- Instancja klasy widoku do której będą przesyłane dane do
                            wyświetlenia użytkownikowi. (default: {None})
        """
        super().__init__()
        self._model = model
        self._view = view

    @abstractmethod
    def get_input(self):
        """Pobiera dane od użytkownika, lub od innej metody które przeprowadzi
            potrzebne obliczenia."""

    @property
    def model(self):
        """Zwraca instancję klasy modelu przekazaną w atrybucie kontruktora.

        Returns:
            [type] -- Instancja klasy modelu.
        """
        return self._model

    @model.setter
    def model(self, value):
        """
        Ustawia nową instancję klasy modelu podanegow konstruktorze.

        Arguments:
            value {[type]} -- Nowa instancja klasy modelu.
        """

        self._model = value

    @property
    def view(self):
        """Zwraca instancję klasy widoku przekazaną w atrybucie kontruktora.

        Returns:
            [type] -- Instancja klasy widoku.
        """
        return self._view

    @view.setter
    def view(self, value):
        """
        Ustawia nową instancję klasy widoku dla klasy.

        Arguments:
            value {View} -- Nowy widok który ma zostać przypisany do kontrolera.
        """
        self._view = value
