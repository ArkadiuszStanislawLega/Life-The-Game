from Controllers.controller import Controller


class SpaceDownEventController(Controller):
    def __init__(self, view, model):
        super().__init__(view=view, model=model)

    def get_input(self):
        if self._model.settings.is_space_pushed:
            if self._model.settings.is_user_change_delay:
                self._model.settings.current_game_delay = self._model.settings.user_game_delay
            else:
                self._model.settings.current_game_delay = self._model.settings.default_game_delay

            self._model.settings.delay_counter = 0
            self._model.settings.is_space_pushed = False
        else:
            self._model.settings.current_game_delay = -1
            self._model.settings.is_space_pushed = True

        self._view.update(self._model.settings.current_game_delay)
        self._view.show()
