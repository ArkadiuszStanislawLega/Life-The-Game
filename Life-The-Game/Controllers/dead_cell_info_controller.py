from Controllers.controller import Controller


class DeadCellInfoController(Controller):
    def __init__(self, view, model):
        super().__init__(view=view, model=model)

    def get_input(self):
        self._view.info_dead_cells_view.update()
        self._view.info_dead_cells_view.show()
