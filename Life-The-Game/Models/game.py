import random

from Models.map import Map
from Models.life_cell import LifeCell
from Models.location import Location
from Models.map_cell import MapCell
from Models.basic_model import BasicModel
from Models.game_settings import GameSettings

#from Library.horizontal_line import horizontal_line
from Library.demonid import demonid
from Library.glider import glider
from Library.spaceship import spaceship
from Library.noah_ark import noah_ark
from Library.info import struct_info
from Library.gosper_glider_gun import gosper_glider_gun


class Game(BasicModel):
    """Model gry w której odbywa się cała rozgrywka."""

    def __init__(self, map_width, map_height):
        super().__init__()
        self.__settings = GameSettings()
        self.__map = Map(width=map_width, height=map_height)
        self.__struct = {"glider": glider,
                         "spaceship": spaceship,
                         "noah_ark": noah_ark,
                         "demonid": demonid,
                         "gosper_glider_gun": gosper_glider_gun}

        self.__dead_cells_to_remove = 0
        self.__cells_that_survive = {}
        self.__cells_that_will_die = []
        self.__cells_for_potential_betting = []
        self.__finded = []
        self.__current_round = 0
        self.__is_working = True
    # region Properties
    @property
    def settings(self):
        return self.__settings

    @settings.setter
    def settings(self, value):
        self.__settings = value

    @property
    def is_working(self):
        return self.__is_working

    @is_working.setter
    def is_working(self, value):
        self.__is_working = value

    @property
    def dead_cells(self):
        """Ilość martwych komórek w rundzie"""
        return self.__dead_cells_to_remove

    @property
    def current_round(self):
        """Aktulny numer rundy"""
        return self.__current_round

    @property
    def map(self):
        """Mapa rozgrywki"""
        return self.__map
        # endregion
    # region Losowanie początkowych struktur i koordynatów

    def gen_random_x(self, struc_info: dict):
        """Generuje losowo x z dostępnych koordynatów na mapie."""
        return random.randrange(0, self.__map.width-struc_info.get("width"))

    def gen_random_y(self, struc_info: dict):
        """Generuje losowo y z dostępnych koordynatów na mapie."""
        return random.randrange(0, self.__map.height-struc_info.get("height"))

    def generate_stuct_in_random_loc(self, name):
        """Generuje komórki w strukture z Library z losową lokalizacją."""
        info = struct_info().get(name)
        self.__struct.get(name)(self, self.gen_random_x(
            info), self.gen_random_y(info))

    def try_generate_struct(self,
                            name: str,
                            max_number_of_struct: int,
                            min_number_of_struct: int,
                            max_chance_to_generate: int):
        """
        Losuje możliwość wylosowania struktury z komórek znajdujących się w
        Library, następnie losuje ich ilość, oraz lokalizację.
        """
        chance = random.randrange(0, max_chance_to_generate)
        if chance < 1000:
            number_of_struct = random.randrange(
                min_number_of_struct, max_number_of_struct)
            for i in range(number_of_struct):
                self.generate_stuct_in_random_loc(name)

    def cells_at_the_begginning(self):
        """
        Początkowy układ komórek przy uruchomieniu aplikacji.
        """

        #horizontal_line(self, 2, 2)
        self.try_generate_struct(name="demonid",
                                 min_number_of_struct=1,
                                 max_number_of_struct=4,
                                 max_chance_to_generate=1500)

        self.try_generate_struct(name="spaceship",
                                 min_number_of_struct=1,
                                 max_number_of_struct=2,
                                 max_chance_to_generate=1500)

        self.try_generate_struct(name="glider",
                                 min_number_of_struct=1,
                                 max_number_of_struct=8,
                                 max_chance_to_generate=1500)

        self.try_generate_struct(name="noah_ark",
                                 min_number_of_struct=1,
                                 max_number_of_struct=2,
                                 max_chance_to_generate=1500)

        self.try_generate_struct(name="gosper_glider_gun",
                                 min_number_of_struct=1,
                                 max_number_of_struct=3,
                                 max_chance_to_generate=1000)
    # endregion

    def put_coordinates_to_map(self, coordinates: list, start_x: int, start_y: int):
        """
        Wstawia komórki życie z listy koordynatów

        Arguments:
            coordinates {list} -- Lista z koordynatami
            start_x -- od której współrzędnej x zaczyna wstawianie komórek
            start_y -- od której współrzędnej y zaczyna wstawianie komórek
        """
        for item in coordinates:
            location = Location()
            location.X = start_x + item[0]
            location.Y = start_y + item[1]
            lifecell = LifeCell()
            lifecell.modify(True)
            lifecell.location = location
            self.put_life_cell(lifecell)

    def __put_new_live_cells(self):
        """
        Dodaje wszystkie nowe żywe komórki w miejscach,
        które zostały wykryte że posiadają 3 sąsiadów.
        """
        for str_location in self.__finded:
            location = self.__map.map_cells_container[str_location].location
            lifecell = LifeCell()
            lifecell.modify(True)
            lifecell.location = location
            self.put_life_cell(lifecell)

    def put_life_cell(self, life_cell: LifeCell):
        """
        Wstawia komórkę życia do określonego pola na mapie.

        Arguments:
            life_cell {LifeCell} -- Komórka życia z ustawionymi koordynatami.
        """
        if isinstance(life_cell, LifeCell) and isinstance(life_cell.location, Location):
            if self.__map.add_life_cell(life_cell):
                self.create_life_cell_view(life_cell)

    def create_life_cell_view(self, life_cell):
        """Tworzy widok żywej komórki i przypisuje do obserowanych modelowi żywej komórki"""
        if isinstance(life_cell, LifeCell):
            game_view = self._obs_list.get("GameView")
            game_view_children = game_view.get_children()
            map_view = ''
            for views in game_view_children:
                if views.name == "MapView":
                    map_view = views
                    break
            life_cell_model = self.__map.life_cells.get(
                f'{life_cell.location}')
            life_cell_view = map_view.add_life_cell_view(life_cell)
            if life_cell_view is not None:
                life_cell_model.add_observer(life_cell_view)

    def run(self):
        """Włącza gre. """
        if self.__is_working:
            self.__check_current_cells_to_see_if_they_survive()
            self.__find_empty_cells_to_live_and_put_new_ones()

            self.__remove_dead_cells()
            self.__clear_after_round()
            self.__current_round += 1

    # region Check fields

    def __clear_after_round(self):
        """Czyści wszystkie właściowści klasy do stanu początkowego rundy."""
        self.__cells_that_survive.clear()
        self.__cells_that_will_die.clear()
        self.__cells_for_potential_betting.clear()
        self.__finded.clear()

    def __search_for_potential_places_to_place_new_cells(self):
        """
        Wyszukuje wszystkie puste miejsca w około aktulnie postawionych komórek na mapie.
        """
        for value in self.__map.life_cells:
            live_cell = self.__map.map_cells_container.get(f'{value}')
            current_location = live_cell.location

            self.__check_top(current_location, False)
            self.__check_mid(current_location, False)
            self.__check_bot(current_location, False)

    def __from_potential_cells_check_which_have_three_neighbors(self):
        """
        Sprawdza czy są 3 komórki w wybranych potencjalnie komórkach.
        Potencjalne komórki które sprawdzam, to wszystkie puste,
        bezpośrednio toważyszące aktualnie żywym i martwym.
        """
        sum_of_neighbors_cells = 0
        counter_of_empty_cells_top = 0
        counter_of_empty_cells_mid = 0
        counter_of_empty_cells_bot = 0

        for str_location in self.__cells_for_potential_betting:
            live_cell = self.__map.map_cells_container.get(str_location)
            location = live_cell.location

            counter_of_empty_cells_top = self.__check_top(location, True)
            counter_of_empty_cells_mid = self.__check_mid(location, True)
            counter_of_empty_cells_bot = self.__check_bot(location, True)

            sum_of_neighbors_cells += counter_of_empty_cells_top + \
                counter_of_empty_cells_mid + counter_of_empty_cells_bot

            if sum_of_neighbors_cells == 3:
                self.__finded.append(f'{location}')

            sum_of_neighbors_cells = 0
            counter_of_empty_cells_top = 0
            counter_of_empty_cells_mid = 0
            counter_of_empty_cells_bot = 0

    def __find_empty_cells_to_live_and_put_new_ones(self):
        """
        Sprawdza pola które miały 3 żywe komórki w około
        siebie i wstawia w odpowiednie miejsce nową żywą komórkę.
        """
        self.__search_for_potential_places_to_place_new_cells()
        self.__from_potential_cells_check_which_have_three_neighbors()
        self.__put_new_live_cells()

    def __remove_dead_cells(self):
        """
        Usuwa martwe komórki z mapy.
        """
        self.__dead_cells_to_remove = len(self.__cells_that_will_die)

        for location in self.__cells_that_will_die:
            map_cell = self.__map.map_cells_container.get(
                f'{location}')
            life_cell_model = self.__map.life_cells.get(f'{location}')
            life_cell_model.notify()
            map_cell.clear_cell()
            del self.__map.life_cells[f'{location}']

    def __check_current_cells_to_see_if_they_survive(self):
        """
        Sprawdza pola wszystkich do okoła komórek aktualnie żywych czy są zdolne do przeżycia.
        """
        count_life_cells_in_neighbors = 0
        counter_cells_in_neighbor_top = 0
        counter_cells_in_neighbor_mid = 0
        counter_cells_in_neighbor_bot = 0

        for cell in self.__map.life_cells.values():
            live_cell = self.__map.map_cells_container.get(
                f'{cell.location}')
            current_location = live_cell.location

            counter_cells_in_neighbor_top = self.__check_top(
                current_location, True)
            counter_cells_in_neighbor_mid = self.__check_mid(
                current_location, True)
            counter_cells_in_neighbor_bot = self.__check_bot(
                current_location, True)

            count_life_cells_in_neighbors += counter_cells_in_neighbor_top + \
                counter_cells_in_neighbor_mid + counter_cells_in_neighbor_bot

            if count_life_cells_in_neighbors in(2, 3):
                self.__cells_that_survive[current_location] = count_life_cells_in_neighbors
                cell.modify(True)
            else:
                self.__cells_that_will_die.append(current_location)
                cell.modify(False)

            count_life_cells_in_neighbors = 0
            counter_cells_in_neighbor_top = 0
            counter_cells_in_neighbor_mid = 0
            counter_cells_in_neighbor_bot = 0

    def __check_bot(self, location, occupied: bool):
        """
        Sprawdza czy w pod koordynatami podanymi w argumencie po lewej,
        środku i po prawo znajdują się jakieś żywe komórki.

        Arguments:
            location {Location} -- koordynaty pod którymi mają zostać sprawdzone pola
            occupied {bool} -- flaga wskazująca czy mają zostaś sprawdzone zajęte pola czy puste

        Returns:
            [int] -- -1 - jeżeli podana w atrybucie lokacja nie jest instancją klasy Location,
                      >= 0 iczba żyjących komórek życia które są pod podanymi koordynatami
        """
        if isinstance(location, Location):
            if location.Y < self.__map.width:
                count_life_cells = 0
                check_location = Location()
                check_location.Y = location.Y+1
                check_location.X = location.X

                left = self.__check_map_cell_left(check_location, occupied)
                mid = self.__check_map_cell_mid(check_location, occupied)
                right = self.__check_map_cell_right(check_location, occupied)

                count_life_cells += left
                count_life_cells += mid
                count_life_cells += right

                return count_life_cells
        else:
            return -1

        return 0

    def __check_mid(self, location, occupied: bool):
        """
        Sprawdza czy na wysokości podanych w argumencie koordynatów
        po lewej i po prawo znajdują się jakieś żywe komórki.

        Arguments:
            location {Location} -- koordynaty w około których mają zostać sprawdzone pola
            occupied {bool} -- flaga wskazująca czy mają zostaś sprawdzone zajęte pola czy puste

        Returns:
            [int] -- -1 - jeżeli podana w atrybucie lokacja nie jest instancją klasy Location,
                      >= liczba żyjących komórek życia po lewej i po prawej stronie.
        """
        if isinstance(location, Location):
            count_life_cells = 0
            count_life_cells += self.__check_map_cell_left(location, occupied)
            count_life_cells += self.__check_map_cell_right(location, occupied)

            return count_life_cells
        else:
            return -1

        return 0

    def __check_top(self, location: Location, occupied: bool):
        """
        Sprawdza czy w nad koordynatami podanymi w argumencie po lewej,
        środku i po prawo znajdują się jakieś żywe komórki.

        Arguments:
            location {Location} -- koordynaty nad którymi mają zostać sprawdzone pola
            occupied {bool} -- flaga wskazująca czy mają zostaś sprawdzone zajęte pola czy puste

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

                count_life_cells += self.__check_map_cell_left(
                    check_location, occupied)
                count_life_cells += self.__check_map_cell_mid(
                    check_location, occupied)
                count_life_cells += self.__check_map_cell_right(
                    check_location, occupied)

                return count_life_cells
        else:
            return -1

        return 0

    def __check_map_cell_left(self, location: Location, occupied: bool):
        """
        Sprawdza komórkę po lewej stronie od podanych koordynatów lokacji
        czy jest zajęta i czy ma komórkę życia aktywną.

        Arguments:
            location {Location} -- koordynaty od których ma zostać srawdzone
                                pole na lewo
            occupied {bool} -- flaga wskazująca czy mają zostaś sprawdzone
                            zajęte pola czy puste

        Returns:
            [int] --  0 - jeżeli lokacja wychodzi po za obszar mapy
                      1 - jeżeli po lewej strony od podanej lokacji pole
                      jest zajęte przez żyjącą komórkę życia
        """
        if isinstance(location, Location) and location.X > 0:
            check_location = Location()
            check_location.Y = location.Y
            check_location.X = location.X-1
            map_cell = self.__map.map_cells_container.get(
                f'{check_location}')
            output = -2
            if occupied:
                output = self.__check_map_cell(map_cell)
            else:
                output = self.__check_is_empty(map_cell)
                if output == 1:
                    if f'{check_location}' not in self.__cells_for_potential_betting:
                        self.__cells_for_potential_betting.append(
                            f'{check_location}')

            return output

        return 0

    def __check_map_cell_mid(self, location: Location, occupied: bool):
        """
        Sprawdza komórkę po na środku  (nad lub pod) od podanych koordynatów
        lokacji czy jest zajęta i czy ma komórkę życia aktywną.

        Arguments:
            location {Location} -- koordynaty od których ma zostać srawdzone
                                pole na środku
            occupied {bool} -- flaga wskazująca czy mają zostaś sprawdzone
                            zajęte pola czy puste

        Returns:
            [int] --  0 - jeżeli lokacja wychodzi po za obszar mapy
                      1 - jeżeli naśrodku (nad lub pod) od podanej
                      lokacji pole jest zajęte przez żyjącą komórkę życia
        """
        if isinstance(location, Location):
            check_location = Location()
            check_location.Y = location.Y
            check_location.X = location.X
            map_cell = self.__map.map_cells_container.get(
                f'{check_location}')
            output = -2
            if occupied:
                output = self.__check_map_cell(map_cell)
            else:
                output = self.__check_is_empty(map_cell)
                if output == 1:
                    if f'{check_location}' not in self.__cells_for_potential_betting:
                        self.__cells_for_potential_betting.append(
                            f'{check_location}')

            return output

        return 0

    def __check_map_cell_right(self, location: Location, occupied: bool):
        """
        Sprawdza komórkę po prawej stronie od podanych koordynatów lokacji
        czy jest zajęta i czy ma komórkę życia aktywną.

        Arguments:
            location {Location} -- koordynaty od których ma zostać srawdzone
                                pole na prawo
            occupied {bool} -- flaga wskazująca czy mają zostaś sprawdzone
                                zajęte pola czy puste

        Returns:
            [int] -- -1 - jeżeli podany w atrybucie element nie jest instancją
                        klasy Lokacja
                      0 - jeżeli lokacja wychodzi po za obszar mapy
                      1 - jeżeli po prawej strony od podanej lokacji pole jest
                        zajęte przez żyjącą komórkę życia
        """
        if isinstance(location, Location):
            if location.X < self.__map.width:
                check_location = Location()
                check_location.Y = location.Y
                check_location.X = location.X+1
                map_cell = self.__map.map_cells_container.get(
                    f'{check_location}')
                output = -2
                if occupied:
                    output = self.__check_map_cell(map_cell)
                else:
                    output = self.__check_is_empty(map_cell)
                    if output == 1:
                        if f'{check_location}' not in self.__cells_for_potential_betting:
                            self.__cells_for_potential_betting.append(
                                f'{check_location}')

                return output
            else:
                return 0
        return -1

    def __check_map_cell(self, map_cell: MapCell):
        """
        Sprawdza czy podane w argumencie pole mapy zawiera w sobie żyjącą
        komórkę życia.

        Arguments:
            map_cell {MapCell} -- pole mapy które ma zostać sprawdzone.

        Returns:
            [int] -- 1 - jeżeli w polu znajduje się żyjąca komórka życia,
                     0 - jeżeli pole may nie posiada żyjącej komórki życia.
        """
        if isinstance(map_cell, MapCell) and isinstance(map_cell.life_cell, LifeCell):
            if map_cell.is_occupied and map_cell.life_cell is not None:
                return 1
        return 0

    def __check_is_empty(self, map_cell: MapCell):
        if isinstance(map_cell, MapCell):
            # Sprawdza czy miejsce jest puste
            if map_cell.is_occupied:
                return 0

            # sprawdza czy miejsce jest zajęte, ale komórka umiera
            if isinstance(map_cell.life_cell, LifeCell) and map_cell.life_cell is not None:
                return 0

            return 1
        return -1
    # endregion

    def modify(self, *args, **kwargs):
        pass

    def notify(self):
        for view in self._obs_list.items():
            view.update()
