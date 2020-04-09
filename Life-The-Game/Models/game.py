from Models.map import Map
from Models.logbook import Logbook
from Models.life_cell import LifeCell
from Models.location import Location
from Models.map_cell import MapCell


class Game(Logbook):
    def __init__(self):
        self.__game_map = Map()
        self.__life_cells = {}

    @property
    def game_map(self):
        return self.__game_map

    def put_life_cell(self, life_cell):
        if isinstance(life_cell, LifeCell) and isinstance(life_cell.location, Location):
            if self.__game_map.container[f'{life_cell.location}'].is_put_life_in_cell(life_cell):
                self.__life_cells[f'{life_cell.location}'] = life_cell

    def find_life_cells(self):
        for value in self.__life_cells.values():
            print(self.check_top(
                self.__game_map.container.get(f'{value.location}').location))

    def check_top(self, location):
        count_life_cells = 0
        check_location = Location()
        check_location.Y = location.Y-1
        check_location.X = location.X

        if isinstance(location, Location):
            if location.Y > 0:
                count_life_cells += self.check_map_cell_left(check_location)
                count_life_cells += self.check_map_cell_mid(check_location)
                count_life_cells += self.check_map_cell_right(check_location)

                if count_life_cells == 3:
                    return 1
        else:
            return -1

        return 0

    def check_map_cell_left(self, location: Location):
        check_location = Location()
        check_location.Y = location.Y
        if isinstance(location, Location) and location.X > 0:
            check_location.X = location.X-1
            eq = self.check_map_cell(
                self.__game_map.container.get(f'{check_location}'))
            print(f'{location} - lewo - {eq}')
            return eq

        return 0

    def check_map_cell_mid(self, location: Location):
        check_location = Location()
        check_location.Y = location.Y
        if isinstance(location, Location):
            check_location.X = location.X
            eq = self.check_map_cell(
                self.__game_map.container.get(f'{check_location}'))
            print(f'{location} - środek - {eq}')
            return eq

        return 0

    def check_map_cell_right(self, location: Location):
        check_location = Location()
        check_location.Y = location.Y
        if isinstance(location, Location) and location.X < self.__game_map.MAP_WIDTH:
            check_location.X = location.X+1
            eq = self.check_map_cell(
                self.__game_map.container.get(f'{check_location}'))
            print(f'{location} - prawo - {eq}')
            return eq
        return 0

    def check_map_cell(self, map_cell: MapCell):
        if isinstance(map_cell, MapCell) and map_cell.is_occupied and isinstance(map_cell.life_cell, LifeCell) and map_cell.life_cell.is_alive:
            return 1
        return 0
