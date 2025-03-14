"""Autor Arkadiusz Łęga email:horemheb@vp.pl"""


from Models.basic_model import BasicModel


class GameSettings(BasicModel):
    """
    Klasa zawiera podstawowe ustawienia rozgrywki.

    Arguments:
        BasicModel {BasicModel} -- Dziedziczy podstawową klase która umożliwia komunikację
                                    pomiędzy kontrolerem a widokiem.
    """

    def __init__(self):
        """Ustawia podstawowe wartości rozgrywki."""
        super().__init__()
        self.__refresh_rate = 60
        self.__delay_counter = 0
        self.__default_game_delay = 1
        self.__user_game_delay = 1
        self.__is_user_change_delay = False
        self.__current_game_delay = 1
        # Flaga wskazująca czy przycisk spacji był wciśnięty
        self.__is_space_pushed = False

    @property
    def refresh_rate(self):
        """
        Wartość wskazująca odświeżanie widoku.

        Returns:
            [int] -- odświeżanie widoku.
        """
        return self.__refresh_rate

    @refresh_rate.setter
    def refresh_rate(self, value):
        self.__refresh_rate = value

    @property
    def default_game_delay(self):
        return self.__default_game_delay

    @default_game_delay.setter
    def default_game_delay(self, value):
        self.__default_game_delay = value

    @property
    def user_game_delay(self):
        return self.__user_game_delay

    @user_game_delay.setter
    def user_game_delay(self, value):
        self.__user_game_delay = value

    @property
    def is_user_change_delay(self):
        return self.__is_user_change_delay

    @is_user_change_delay.setter
    def is_user_change_delay(self, value):
        self.__is_user_change_delay = value

    @property
    def is_space_pushed(self):
        return self.__is_space_pushed

    @is_space_pushed.setter
    def is_space_pushed(self, value):
        self.__is_space_pushed = value

    @property
    def current_game_delay(self):
        return self.__current_game_delay

    @current_game_delay.setter
    def current_game_delay(self, value):
        self.__current_game_delay = value

    @property
    def delay_counter(self):
        return self.__delay_counter

    @delay_counter.setter
    def delay_counter(self, value):
        self.__delay_counter = value

    def modify(self, *args, **kwargs):
        pass

    def notify(self):
        pass
