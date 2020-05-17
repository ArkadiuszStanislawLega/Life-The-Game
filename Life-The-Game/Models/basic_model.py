from abc import ABC, abstractmethod


class BasicModel(ABC):
    """
    Abstrakcyjna klasa modelu od której powinien dziedziczyć każdy model
    do którego będzie można podpiąć kontroller i widok.

    Arguments:
        ABC {[type]} -- [description]
    """

    def __init__(self):
        """
        Tworzy słownik z elementami widoku które będa obserwować ten model.
        """
        super().__init__()
        self._obs_list = dict()

    @property
    def obs_list(self):
        """
        Zwraca słownik z obseratorami modelu.

        Returns:
            [dict] -- Słownik z obserwatorami modelu.
        """
        return self._obs_list

    def add_observer(self, obs):
        """
        Dodaje obserwatora do słownika.

        Arguments:
            obs {View} -- Widok który obserwuje ten model.
        """
        if obs.name not in self._obs_list:
            self._obs_list[obs.name] = obs

    def remove_observer(self, name):
        """
        Usuwa obserwatora ze słownika.

        Arguments:
            name {str} -- Nazwa wiodku w słowniku.
        """
        if name in self._obs_list:
            del self._obs_list[name]

    @abstractmethod
    def modify(self, *args, **kwargs):
        """Dzięki tej metodzie będzie można zmieniać właściwości klasy
        które są obserwowane przez obserwatorów."""
        pass

    @abstractmethod
    def notify(self):
        """Przesyła informacje do widoków w słowniku które obserwują klase
        żeby zaktualizowały widok.
        """
        pass
