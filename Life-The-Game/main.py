from Models.game import Game
from Views.game_view import GameView
from Controllers.game_controller import GameController


class App():
    """
    stko zaczyna.
    Przy takich ustawieniach mapa działa na cały ekran przy rozdzielczości 1366x768 ekran 15"
    GAME_WIDTH = 137
    GAME_HEIGHT = 73
    """
    GAME_WIDTH = 137
    GAME_HEIGHT = 73

    def __init__(self):
        self.__model = Game(map_width=self.GAME_WIDTH,
                            map_height=self.GAME_HEIGHT)

        self.__view = GameView(self.__model)
        self.__model.add_observer(self.__view)

        self.__controller = GameController(model=self.__model,
                                           view=self.__view)

        self.__controller.start_game()

    @property
    def model(self):
        return self.__model

    @property
    def view(self):
        return self.__view

    @property
    def controller(self):
        return self.__controller


def main():
    App()


if __name__ == "__main__":
    main()
