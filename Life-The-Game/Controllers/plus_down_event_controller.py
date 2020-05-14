from Controllers.controller import Controller


class PlusDownEventController(Controller):
    def __init__(self, view, model):
        super().__init__(view=view, model=model)

    def get_input(self):
        self._model.settings.is_user_change_delay = True
        self._model.settings.user_game_delay += 1
        self._model.settings.delay_counter = 0
        self._model.settings.current_game_delay = self._model.settings.user_game_delay
        self._view.update(self._model.settings.current_game_delay)
        self._view.show()
