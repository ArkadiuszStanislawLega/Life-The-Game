from Controllers.controller import Controller
from Controllers.life_cell_info_controller import LifeCellInfoController


class GameController(Controller):
    def __init__(self, view, model):
        super().__init__(view=view, model=model)

        self.__life_cell_info_controller = LifeCellInfoController(
            model=len(self._model.life_cells), view=view)

    def get_life_cell_input(self):
        self.__life_cell_info_controller.get_input()

    def get_input(self):
        self.get_life_cell_input()
