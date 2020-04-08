from Models.log import Log


class Logbook:
    PRINT_LOG = True
    __logs = {}

    def _add_log(self, message: str):
        log = Log(message)
        self.__logs[log.date] = log
        if self.PRINT_LOG:
            print(log)

    @property
    def logs(self):
        return self.__logs
