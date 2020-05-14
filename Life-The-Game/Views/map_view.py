from Views.view import View
from Views.map_cell_view import MapCellView
from Views.life_cell_view import LifeCellView
from Views.map_settings import MapSettings


class MapView(View):
    """
    Klasa reprezentująca widok wszystkich komórek z których jest złożona mapa.
    """

    def __init__(self, model, screen, cell_width=10, cell_height=10):
        super().__init__(name="MapView", model=model)
        self.__settings = MapSettings(cell_width, cell_height)
        self.__screen = screen
        self.__create_map()

    def __create_map(self):
        """
        Dodaje wszystkie widoki komórek które są utworzone w instancji gry.
        """
        for key, value in self._model.map_cells_container.items():
            if not self._component_list.get(key):
                view = MapCellView(screen=self.__screen, model=value)
                value.add_observer(view)
                self.add_component(view)

    def add_component(self, comp):
        if comp.name not in self._component_list:
            self._component_list[comp.name] = comp

    def add_life_cell_view(self, model):
        new_life_cell_name = f'LifeCellView:{model.name}'
        if not self._component_list.get(new_life_cell_name):
            view = LifeCellView(screen=self.__screen,
                                model=model,
                                width=self.__settings.cell_width,
                                height=self.__settings.cell_height)
            view.name = new_life_cell_name
            self.add_component(view)
            return view

    def remove_dead_life_cell_view(self, life_cell_view: LifeCellView):
        self.remove_component(life_cell_view)

    def update_life_cell_view(self, life_cell_view):
        self._component_list.get(f'{life_cell_view}').update(life_cell_view)

    def update(self, *args, **kwargs):
        pass

    def show(self):
        for map_cell in self._component_list.values():
            map_cell.show()
