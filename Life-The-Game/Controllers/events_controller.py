import pygame
from Controllers.controller import Controller
from Controllers.minus_down_event_controller import MinusDownEventController
from Controllers.plus_down_event_controller import PlusDownEventController
from Controllers.space_down_event_controller import SpaceDownEventController


class EventsController(Controller):
    def __init__(self, view, model):
        super().__init__(view=view, model=model)

        self.__minus_down_event = MinusDownEventController(model=self._model,
                                                           view=self._view.texts.info_game_delay)

        self.__plus_down_event = PlusDownEventController(model=self._model,
                                                         view=self._view.texts.info_game_delay)

        self.__space_down_event = SpaceDownEventController(model=self._model,
                                                           view=self._view.texts.info_game_delay)

    def get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._model.is_working = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.__space_down_event.get_input()

                if event.key == pygame.K_KP_PLUS or event.key == pygame.K_PLUS:
                    self.__plus_down_event.get_input()

                if event.key == pygame.K_KP_MINUS or event.key == pygame.K_MINUS:
                    self.__minus_down_event.get_input()
