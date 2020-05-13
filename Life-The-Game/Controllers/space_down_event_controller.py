from Controllers.controller import Controller


class SpaceDownEventController(Controller):
    def __init__(self, view, model):
        super().__init__(view=view, model=model)

    def get_input(self):
        if self._model.is_space_pushed:
            if self._model.is_user_change_delay:
                self._model.current_game_delay = self._model.user_game_delay
            else:
                self._model.current_game_delay = self._model.default_game_delay

            self._model.delay_counter = 0
            self._model.is_space_pushed = False
        else:
            self._model.current_game_delay = -1
            self._model.is_space_pushed = True
            self._model.text_view.print_text()

        self._view.update()
        self._view.show()
