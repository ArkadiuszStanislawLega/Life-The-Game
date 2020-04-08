class Location:
    def __init__(self):
        self.__x = 0
        self.__y = 0

    @property
    def X(self):
        return self.__x

    @property
    def Y(self):
        return self.__y

    def __str__(self):
        return f'({self.__x}, {self.__y})'
