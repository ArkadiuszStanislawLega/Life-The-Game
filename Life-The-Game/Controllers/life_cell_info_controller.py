from Controllers.controller import Controller


class LifeCellInfoController(Controller):
    def __init__(self, view, model):
        super().__init__(view=view, model=model)

    def get_input(self):
        self._view.info_life_cells_view.update()
        self._view.info_life_cells_view.show()
