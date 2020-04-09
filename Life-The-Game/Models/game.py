from Models.map import Map
from Models.logbook import Logbook
from Models.life_cell import LifeCell
from Models.location import Location
from Models.map_cell import MapCell


class Game(Logbook):
    def __init__(self):
        self.__game_map = Map()
        self.__life_cells = {}

        self.__cells_that_survive = {}
        self.__cells_that_will_die = []

    @property
    def game_map(self):
        return self.__game_map

    def remove_dead_cells(self):
        for location in self.__cells_that_will_die:
            cell = self.__game_map.container.get(f'{location}')
            cell.clear_cell()

        self.__cells_that_will_die.clear()

    def put_life_cell(self, life_cell: LifeCell):
        """
        Wstawia komórkę życia do określonego pola na mapie.

        Arguments:
            life_cell {LifeCell} -- Komórka życia z ustawionymi koordynatami.
        """
        if isinstance(life_cell, LifeCell) and isinstance(life_cell.location, Location):
            if self.__game_map.container.get(f'{life_cell.location}').is_put_life_in_cell(life_cell):
                self.__life_cells[f'{life_cell.location}'] = life_cell

    def find_life_cells(self):
        """
        Sprawdza pola wszystkich do okoła komórek aktualnie żywych czy są zdolne do przeżycia.
        """
        count_life_cells = 0
        counter_top = 0
        counter_mid = 0
        counter_bot = 0
        counter = 0
        for value in self.__life_cells.values():
            live_cell = self.__game_map.container.get(f'{value.location}')
            current_location = live_cell.location
            # print(f'Sprawdzam komórkę: {counter+1} - {current_location}')

            counter_top = self.check_top(current_location)
            # print(f'góra - {counter_top}')

            counter_mid = self.check_mid(current_location)
            # print(f'środek - {counter_mid}')

            counter_bot = self.check_bot(current_location)
            # print(f'dół - {counter_bot}')

            count_life_cells += counter_top + counter_mid + counter_bot

            if count_life_cells == 2 or count_life_cells == 3:
                self.__cells_that_survive[current_location] = count_life_cells
            #    value.is_alive = True
            else:
                self.__cells_that_will_die.append(current_location)
            #    value.is_alive = False

            count_life_cells = 0
            counter_top = 0
            counter_mid = 0
            counter_bot = 0

            counter += 1

        print("Przeżyją:")
        cnt = 1
        for item in self.__cells_that_survive:
            print(f'{cnt}. {item} {self.__cells_that_survive[item]}')
            cnt += 1

        print("Umrą:")
        for i, item in enumerate(self.__cells_that_will_die):
            print(f'{i+1}. {item}')

    def check_bot(self, location):
        """
        Sprawdza czy w pod koordynatami podanymi w argumencie po lewej, środku i po prawo znajdują się jakieś żywe komórki.

        Arguments:
            location {Location} -- koordynaty pod którymi mają zostać sprawdzone pola

        Returns:
            [int] -- -1 - jeżeli podana w atrybucie lokacja nie jest instancją klasy Location,
                      >= 0 iczba żyjących komórek życia które są pod podanymi koordynatami
        """
        if isinstance(location, Location):
            if location.Y < self.__game_map.MAP_WIDTH:
                count_life_cells = 0
                check_location = Location()
                check_location.Y = location.Y+1
                check_location.X = location.X

                count_life_cells += self.__check_map_cell_left(check_location)
                count_life_cells += self.__check_map_cell_mid(check_location)
                count_life_cells += self.__check_map_cell_right(check_location)

                return count_life_cells
        else:
            return -1

        return 0

    def check_mid(self, location):
        """
        Sprawdza czy na wysokości podanych w argumencie koordynatów po lewej i po prawo znajdują się jakieś żywe komórki.

        Arguments:
            location {Location} -- koordynaty w około których mają zostać sprawdzone pola

        Returns:
            [int] -- -1 - jeżeli podana w atrybucie lokacja nie jest instancją klasy Location,
                      >= liczba żyjących komórek życia po lewej i po prawej stronie.
        """
        if isinstance(location, Location):
            count_life_cells = 0
            count_life_cells += self.__check_map_cell_left(location)
            count_life_cells += self.__check_map_cell_right(location)

            return count_life_cells
        else:
            return -1

        return 0

    def check_top(self, location: Location):
        """
        Sprawdza czy w nad koordynatami podanymi w argumencie po lewej, środku i po prawo znajdują się jakieś żywe komórki.

        Arguments:
            location {Location} -- koordynaty nad którymi mają zostać sprawdzone pola

        Returns:
            [int] -- -1 - jeżeli podana w atrybucie lokacja nie jest instancją klasy Location,
                      >= 0 iczba żyjących komórek życia które są nad podanymi koordynatami
        """
        if isinstance(location, Location):
            if location.Y > 0:
                count_life_cells = 0
                check_location = Location()
                check_location.Y = location.Y-1
                check_location.X = location.X

                count_life_cells += self.__check_map_cell_left(check_location)
                count_life_cells += self.__check_map_cell_mid(check_location)
                count_life_cells += self.__check_map_cell_right(check_location)

                return count_life_cells
        else:
            return -1

        return 0

    def __check_map_cell_left(self, location: Location):
        """
        Sprawdza komórkę po lewej stronie od podanych koordynatów lokacji czy jest zajęta i czy ma komórkę życia aktywną.

        Arguments:
            location {Location} -- koordynaty od których ma zostać srawdzone pole na lewo

        Returns:
            [int] -- -1 - jeżeli podany w atrybucie element nie jest instancją klasy Lokacja
                      0 - jeżeli lokacja wychodzi po za obszar mapy
                      1 - jeżeli po lewej strony od podanej lokacji pole jest zajęte przez żyjącą komórkę życia
        """
        if isinstance(location, Location) and location.X > 0:
            check_location = Location()
            check_location.Y = location.Y
            check_location.X = location.X-1
            map_cell = self.__game_map.container.get(f'{check_location}')
            eq = self.check_map_cell(map_cell)

            # debug help
            # print(f'{check_location} - lewo - {eq}')
            return eq

        return 0

    def __check_map_cell_mid(self, location: Location):
        """
        Sprawdza komórkę po na środku  (nad lub pod) od podanych koordynatów lokacji czy jest zajęta i czy ma komórkę życia aktywną.

        Arguments:
            location {Location} -- koordynaty od których ma zostać srawdzone pole na środku

        Returns:
            [int] -- -1 - jeżeli podany w atrybucie element nie jest instancją klasy Lokacja
                      0 - jeżeli lokacja wychodzi po za obszar mapy
                      1 - jeżeli naśrodku (nad lub pod) od podanej lokacji pole jest zajęte przez żyjącą komórkę życia
        """
        if isinstance(location, Location):
            check_location = Location()
            check_location.Y = location.Y
            check_location.X = location.X
            map_cell = self.__game_map.container.get(f'{check_location}')
            eq = self.check_map_cell(map_cell)

            # debug help
            # print(f'{check_location} - środek - {eq}')
            return eq

        return 0

    def __check_map_cell_right(self, location: Location):
        """
        Sprawdza komórkę po prawej stronie od podanych koordynatów lokacji czy jest zajęta i czy ma komórkę życia aktywną.

        Arguments:
            location {Location} -- koordynaty od których ma zostać srawdzone pole na prawo

        Returns:
            [int] -- -1 - jeżeli podany w atrybucie element nie jest instancją klasy Lokacja
                      0 - jeżeli lokacja wychodzi po za obszar mapy
                      1 - jeżeli po prawej strony od podanej lokacji pole jest zajęte przez żyjącą komórkę życia
        """
        if isinstance(location, Location):
            if location.X < self.__game_map.MAP_WIDTH:
                check_location = Location()
                check_location.Y = location.Y
                check_location.X = location.X+1
                map_cell = self.__game_map.container.get(f'{check_location}')
                eq = self.check_map_cell(map_cell)

                # debug help
                # print(f'{check_location} - prawo - {eq}')
                return eq
            else:
                return 0
        return -1

    def check_map_cell(self, map_cell: MapCell):
        """
        Sprawdza czy podane w argumencie pole mapy zawiera w sobie żyjącą komórkę życia.

        Arguments:
            map_cell {MapCell} -- pole mapy które ma zostać sprawdzone.

        Returns:
            [int] -- 1 - jeżeli w polu znajduje się żyjąca komórka życia, 0 - jeżeli pole may nie posiada żyjącej komórki życia.
        """
        if isinstance(map_cell, MapCell) and map_cell.is_occupied and isinstance(map_cell.life_cell, LifeCell) and map_cell.life_cell.is_alive:
            return 1
        return 0
