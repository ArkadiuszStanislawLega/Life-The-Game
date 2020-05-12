from Models.location import Location
from Models.basic_model import BasicModel


class LifeCell(BasicModel):
    CHARACTER_REPRESENTING_AN_LIVE_CELL = 'O'
    CHARACTER_REPRESENTING_AN_DEAD_CELL = 'X'

    def __init__(self):
        super().__init__()
        self.__is_alive = False
        self.__location = Location()
        self.__name = ""

    def __str__(self):
        if self.__is_alive:
            return self.CHARACTER_REPRESENTING_AN_LIVE_CELL
        return self.CHARACTER_REPRESENTING_AN_DEAD_CELL

    @property
    def name(self):
        return f'{self.__location}'

    @property
    def location(self):
        return self.__location

    @property
    def is_alive(self):
        return self.__is_alive

    @is_alive.setter
    def is_alive(self, value: bool):
        self.__is_alive = value
        self.modify()

    @location.setter
    def location(self, value):
        self.__location = value

    def modify(self, *args, **kwargs):
        self.__is_alive = False

        self.notify()

    def notify(self):
        if self._obs_list.get(f'MapCellView:{self.__location}'):
            self._obs_list.get(f'MapCellView:{self.__location}').update(
                key='LifeCell', value=self)
