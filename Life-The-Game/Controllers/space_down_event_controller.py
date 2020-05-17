from Controllers.controller import Controller


class SpaceDownEventController(Controller):
    """
    Kontroller odpowiedzialny za przechwytwanie wciśnięcie klawisza spacji.

    Arguments:
        Controller {Controller} --  Interfejs umożliwający połączenie widoku z modelem.
    """

    def __init__(self, view, model):
        """
        Inicjuje właściowści które dziedziczy z klasy Controller.

        Arguments:
            view {View} -- Widok do którego mają zostać przekazane dane.
            model {[type]} -- Model z którego są pobierane dane do przeprowadzenia zmian
                            a później wyświetlenia tych danych na ekranie użytkownika.
        """
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
