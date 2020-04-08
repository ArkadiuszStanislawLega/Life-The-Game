from Models.map import Map


class Game:
    def __init__(self):
        self.__game_map = Map()

    @property
    def game_map(self):
        return self.__game_map

    def put_life_cell(self, life_cell):
        self.__game_map.container[f'{life_cell.location}'].is_put_life_in_cell(
            life_cell)
