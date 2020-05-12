from Views.view import View
from Views.map_cell_view import MapCellView
from Views.life_cell_view import LifeCellView


class MapView(View):
    """
    Klasa reprezentująca widok wszystkich komórek z których jest złożona mapa.
    """

    def __init__(self, model, screen):
        super().__init__(name="MapView", model=model)
        self.__screen = screen
        self.__create_map()
        pass

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

    def update(self, *args, **kwargs):
        if len(kwargs) > 0:
            key = kwargs.get("key")
            value = kwargs.get("value")

            if key == "NewLifeCell":
                new_life_cell_name = ""
                new_life_cell_name += f'{value.name}'
                if not self._component_list.get(new_life_cell_name):
                    self._component_list.update({new_life_cell_name: value})

            elif key == "RemoveLifeCell":
                life_cell_to_remove_name = f'LifeCellView:{value.life_cell.name}'
                self.remove_component(life_cell_to_remove_name)

            else:
                for key in kwargs.values():
                    self._component_list.get(key).update()

    def show(self):
        for map_cell in self._component_list.values():
            map_cell.show()
