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
            if self.__game_map.container.get(f'{life_cell.location}').is_put_life_in_cell(life_cell):
                self.__life_cells[f'{life_cell.location}'] = life_cell

    def find_life_cells(self):
        count_life_cells = 0
        counter_top = 0
        counter_mid = 0
        counter_bot = 0
        counter = 0
        for value in self.__life_cells.values():
            current_location = self.__game_map.container.get(
                f'{value.location}').location
            #print(f'Sprawdzam komórkę: {counter+1} - {current_location}')

            counter_top = self.check_top(current_location)
            #print(f'góra - {counter_top}')

            counter_mid = self.check_mid(current_location)
            #print(f'środek - {counter_mid}')

            counter_bot = self.check_bot(current_location)
            #print(f'dół - {counter_bot}')

            count_life_cells += counter_top + counter_mid + counter_bot

            if count_life_cells == 3:
                value.is_alive = True
            else:
                value.is_alive = False

            counter += 1
            print()

    def check_bot(self, location):
        if isinstance(location, Location):
            count_life_cells = 0
            check_location = Location()
            check_location.Y = location.Y+1
            check_location.X = location.X
            if location.Y > 0:
                count_life_cells += self.check_map_cell_left(check_location)
                count_life_cells += self.check_map_cell_mid(check_location)
                count_life_cells += self.check_map_cell_right(check_location)

                return count_life_cells
        else:
            return -1

        return 0

    def check_mid(self, location):
        if isinstance(location, Location):
            count_life_cells = 0
            count_life_cells += self.check_map_cell_left(location)
            count_life_cells += self.check_map_cell_right(location)

            return count_life_cells
        else:
            return -1

        return 0

    def check_top(self, location):
        if isinstance(location, Location):
            count_life_cells = 0
            check_location = Location()
            check_location.Y = location.Y-1
            check_location.X = location.X
            if location.Y > 0:
                count_life_cells += self.check_map_cell_left(check_location)
                count_life_cells += self.check_map_cell_mid(check_location)
                count_life_cells += self.check_map_cell_right(check_location)

                return count_life_cells
        else:
            return -1

        return 0

    def check_map_cell_left(self, location: Location):
        if isinstance(location, Location) and location.X > 0:
            check_location = Location()
            check_location.Y = location.Y
            check_location.X = location.X-1
            map_cell = self.__game_map.container.get(f'{check_location}')
            eq = self.check_map_cell(map_cell)

            #print(f'{check_location} - lewo - {eq}')
            return eq

        return 0

    def check_map_cell_mid(self, location: Location):
        if isinstance(location, Location):
            check_location = Location()
            check_location.Y = location.Y
            check_location.X = location.X
            map_cell = self.__game_map.container.get(f'{check_location}')
            eq = self.check_map_cell(map_cell)
            #print(f'{check_location} - środek - {eq}')
            return eq

        return 0

    def check_map_cell_right(self, location: Location):
        if isinstance(location, Location) and location.X < self.__game_map.MAP_WIDTH:
            check_location = Location()
            check_location.Y = location.Y
            check_location.X = location.X+1
            map_cell = self.__game_map.container.get(f'{check_location}')
            eq = self.check_map_cell(map_cell)
            #print(f'{check_location} - prawo - {eq}')
            return eq
        return 0

    def check_map_cell(self, map_cell: MapCell):
        if isinstance(map_cell, MapCell) and map_cell.is_occupied and isinstance(map_cell.life_cell, LifeCell) and map_cell.life_cell.is_alive:
            return 1
        return 0
