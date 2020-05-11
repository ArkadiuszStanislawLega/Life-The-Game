from Views.view import View
from Views.map_cell_view import MapCellView


class MapView(View):
    def __init__(self, model, screen):
        super().__init__(name="MapView", model=model)
        self.__screen = screen
        self.__create_map()
        pass

    def __create_map(self):
        """
        Dodaje wszystkie widoki komórek które są utworzone w instancji gry.
        """
        for key, value in self._model.container.items():
            if not self._component_list.get(key):
                view = MapCellView(screen=self.__screen, model=value)
                value.add_observer(view)
                self.add_component(view)

    def add_component(self, comp):
        if comp.name not in self._component_list:
            self._component_list[comp.name] = comp

    def update(self, *args, **kwargs):
        for key in kwargs.values():
            self._component_list.get(key).update()

    def show(self):
        pass
