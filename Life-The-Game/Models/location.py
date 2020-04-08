class Location:
    def __init__(self):
        self.__x = 0
        self.__y = 0

    @property
    def X(self):
        return self.__x

    @X.setter
    def X(self, value):
        self.__x = value

    @property
    def Y(self):
        return self.__y

    @Y.setter
    def Y(self, value):
        self.__y = value

    def __str__(self):
        return f'({self.__x}, {self.__y})'
