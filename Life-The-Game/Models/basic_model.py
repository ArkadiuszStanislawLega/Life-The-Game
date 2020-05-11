from abc import ABC, abstractmethod


class BasicModel(ABC):
    def __init__(self):
        super().__init__()
        self._obs_list = dict()

    @property
    def obs_list(self):
        return self._obs_list

    def add_observer(self, obs):
        if obs.name not in self._obs_list:
            self._obs_list[obs.name] = obs

    def remove_observer(self, name):
        if name in self._obs_list:
            del self._obs_list[name]

    @abstractmethod
    def modify(self, *args, **kwargs):
        pass

    @abstractmethod
    def notify(self):
        pass
