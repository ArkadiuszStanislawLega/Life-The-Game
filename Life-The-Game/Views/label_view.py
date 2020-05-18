"""Autor: Arkadiusz Łęga, email:horemheb@vp.pl"""
from Views.view import View
from Views.text_settings import TextSettings


class LabelView(View):
    """Widok jednego wiersza tekstu.

    Arguments:
        View {View} -- klasa widoku ułatwia połączenie modelu z widokiem.
    """

    def __init__(self, screen, model=1, text="", name="LabelView"):
        """W czasie inicjalizacji zostaje wygnerowane ciało tekstu przy użyciu biblioteki
        pygame.

        Arguments:
            screen {pygame} -- główne okno aplikacji.

        Keyword Arguments:
            model {int} -- model z którego mają być pobierane dane. Wartość jest
                            wtyświetlana po wartości tekstu podanego w atrybucie. (default: {1})
            text {str} -- tekst który ma być wyświetlony przed wartością z modelu. (default: {""})
            name {str} -- nazwa widoku, po której jest wyszukiwany widok.
                            Dla poprawnego działa w jednym gridzie lub przy zastosowaniu
                            jak kolejny komponent w widoku musi być uniaktowa, należy nadać
                            unikatowe nazwy dla każdego. (default: {"LabelView"})
        """
        super().__init__(name=name, model=model)
        self.__screen = screen
        self.__text = text
        self.__full_text = f'{self.__text}{self._model}'
        self.__settings = TextSettings()
        self.__body = self.__settings.font.render(self.__full_text,
                                                  False,
                                                  self.__settings.font_colour)

    @property
    def settings(self):
        """Udostępnia podstawowe ustawienia etykiety.

        Returns:
            [TextSettings] -- podastawowe ustawienia etykiety.
        """
        return self.__settings

    @settings.setter
    def settings(self, value):
        """Umożliwia zmianę ustawień etykiety.

        Arguments:
            value {[TextSettings]} -- nowe podstawowe ustawienia.
        """
        self.__settings = value

    def add_component(self, comp):
        if comp.name not in self._component_list:
            self._component_list[comp.name] = comp

    def update(self, *args, **kwargs):
        if len(args) > 0:
            self._model = args[0]
            self.__full_text = f'{self.__text}{self._model}'
            self.__body = self.__settings.font.render(self.__full_text,
                                                      True,
                                                      self.__settings.font_colour,
                                                      self.__settings.background_colour)

    def show(self):
        self.__body = self.__settings.font.render(self.__full_text,
                                                  True,
                                                  self.__settings.font_colour,
                                                  self.__settings.background_colour)

        self.__screen.blit(self.__body, (self.__settings.left_margin,
                                         self.__settings.coordinate_y))
