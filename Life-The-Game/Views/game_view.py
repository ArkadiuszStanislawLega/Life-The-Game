"""Autor: Arkadiusz Łęga, email:horemheb@vp.pl"""
import pygame
from Views.view_settings import ViewSettings
from Views.view import View
from Views.map_view import MapView
from Views.text_views import TextViews


class GameView(View):
    """Klasa przetrzymuje wszystkie widoki potrzebne do przeprowadzenia rozgrywki."""

    def __init__(self, model):
        super().__init__(name="GameView", model=model)
        self.__settings = ViewSettings(self._model)
        self.__screen = pygame.display.set_mode(self.__settings.window_size)

        self.__map = MapView(model=self._model.map,
                             screen=self.__screen,
                             cell_width=self.__settings.cell_width,
                             cell_height=self.__settings.cell_height)
        self.add_component(self.__map)

        pygame.init()
        pygame.display.set_caption(self.__settings.window_title)

        self.__texts = TextViews(model=self._model, screen=self.__screen)
        self.add_component(self.__texts)

        self._model.map.add_observer(self.__map)

        self.show()

    def round(self):
        """Akcje podczas jednego przebiegu rozgrywki.
        Odświeżenie tekstu i usunięcie martwych komórek z mapy.
        """
        self.__texts.round()
        self.__map.round()

    @property
    def map(self):
        """Widok mapy wyświetlanej użytkownikowi.

        Returns:
            [MapView] -- widok rozgrywki.
        """
        return self.__map

    @property
    def texts(self):
        """Widok wszystkich tekstów które są wyświetlane w czasie rozgrywki.

        Returns:
            [TextsView] -- Widok wszystkich tekstów widocznych w czasie rozgrywki.
        """
        return self.__texts

    @property
    def screen(self):
        """Instancja okna pygame.

        Returns:
            [pygame] -- Instancja okna pygame.
        """
        return self.__screen

    def add_component(self, comp):
        if comp.name not in self._component_list:
            self._component_list[comp.name] = comp

    def update(self, *args, **kwargs):
        pass

    def show(self):
        """Wyświetla wszystkie komponenty wchodzące wskład gry."""
        for view in self._component_list.values():
            view.show()
