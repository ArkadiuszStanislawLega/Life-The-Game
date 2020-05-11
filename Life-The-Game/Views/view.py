from abc import ABC, abstractmethod


class View(ABC):
    def __init__(self, name, model):
        super().__init__()
        self._name = name
        self._component_list = dict()
        self._model = model

    @property
    def name(self):
        return self._name

    def get_children(self):
        return self._component_list.values()

    def remove_component(self, name):
        if name in self._component_list:
            del self._component_list[name]

    @abstractmethod
    def add_component(self, comp):
        if comp.name not in self._component_list:
            self._component_list[comp.name] = comp

    @abstractmethod
    def update(self, *args, **kwargs):
        pass

    @abstractmethod
    def show(self):
        pass
