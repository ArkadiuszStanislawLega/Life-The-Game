import datetime


class Log:

    def __init__(self, message):
        self._date = datetime.datetime.now()
        self._message = message

    def __str__(self):
        return f'{self._date.strftime("%d-%m-%Y %X")} - {self._message}'

    def __repr__(self):
        return self.__str__()

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date
