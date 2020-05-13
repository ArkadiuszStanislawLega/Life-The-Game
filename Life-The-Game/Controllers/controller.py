from abc import ABC, abstractmethod


class Controller(ABC):
    def __init__(self, model=None, view=None):
        super().__init__()
        self._model = model
        self._view = view

    @abstractmethod
    def get_input(self):
        pass

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def view(self):
        return self._view

    @view.setter
    def view(self, value):
        self._view = value
