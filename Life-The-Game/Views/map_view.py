"""Autor: Arkadiusz Łęga, email:horemheb@vp.pl"""
from Views.view import View
from Views.map_cell_view import MapCellView
from Views.life_cell_view import LifeCellView
from Views.map_settings import MapSettings
from Models.life_cell import LifeCell


class MapView(View):
    """Klasa reprezentująca widok wszystkich komórek z których jest złożona mapa."""

    def __init__(self, model, screen, cell_width=10, cell_height=10):
        """Ustawia podstawe wartość widoku mapy na podstawie podanych
        wartość w argumentach. Tworzy i wyświetla mapę na ekranie.
        Kontroluje widok wszystkich widoków komórek przewidzianych w
        czasie prowadzenia rozgrywki.

        Arguments:
            model {Map} -- instancja klasy Map używana w czasie rozgrywki
                            sterowanej przez instancje klasy Game.
            screen {pygame} -- główny widok okna.

        Keyword Arguments:
            cell_width {int} -- szerokość pojedynczej komórki podana w
                                pikselach (default: {10})
            cell_height {int} -- wysokość pojednyczej komórki podana w
                                pikselach (default: {10})
        """
        super().__init__(name="MapView", model=model)
        self.__settings = MapSettings(cell_width, cell_height)
        self.__screen = screen
        self.__create_map()

    def round(self):
        """Akcja przewidziana w przeciągu przebiegu jednej rundy rozgrywki."""
        self.remove_dead_cells_views()

    def __create_map(self):
        """
        Dodaje wszystkie widoki komórek które są utworzone w instancji gry.
        """
        for key, value in self._model.map_cells_container.items():
            if not self._component_list.get(key):
                view = MapCellView(screen=self.__screen, model=value)
                value.add_observer(view)
                self.add_component(view)

    def add_life_cell_view(self, model: LifeCell):
        """Dodaje nowy widok komórki życia do widoku mapy.

        Arguments:
            model {LifeCell} -- model żywej komórki którego
                                widok ma zostać dodany do widoku mapy.

        Returns:
            [LifeCellView] -- widok żywej komórki.
        """

        if isinstance(model, LifeCell):
            new_life_cell_name = f'LifeCellView:{model.name}'
            if not self._component_list.get(new_life_cell_name):
                view = LifeCellView(screen=self.__screen,
                                    model=model,
                                    width=self.__settings.cell_width,
                                    height=self.__settings.cell_height)
                view.name = new_life_cell_name
                self.add_component(view)
                return view

        return None

    def print_life_cells(self):
        """Drukuje wszystkie widoki żywych komórek na mapie."""
        for life_cell in self._component_list.values():
            if isinstance(life_cell, LifeCellView) and life_cell.model.is_alive:
                life_cell.show()

    def remove_dead_cells_views(self):
        """Usuwa wszystkie widoki martwych komórek z mapy."""
        dead_views = []
        for map_cell in self._component_list.values():
            if isinstance(map_cell, LifeCellView):
                if not map_cell.model.is_alive:
                    dead_views.append(map_cell.name)

        for dead in dead_views:
            self.remove_component(dead)

        dead_views.clear()

    def add_component(self, comp):
        if comp.name not in self._component_list:
            self._component_list[comp.name] = comp

    def update(self, *args, **kwargs):
        pass

    def show(self):
        for map_cell in self._component_list.values():
            if isinstance(map_cell, LifeCellView):
                map_cell.show()
