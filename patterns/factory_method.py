from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass


class ConsoleLogger(Logger):
    def log(self, message):
        print("Console:", message)


class FileLogger(Logger):
    def log(self, message):
        print("File:", message)


class LoggerFactory(ABC):
    @abstractmethod
    def create_logger(self):
        pass

    def log_message(self, message):
        logger = self.create_logger()
        logger.log(message)


class ConsoleLoggerFactory(LoggerFactory):
    def create_logger(self):
        return ConsoleLogger()


if __name__ == "__main__":
    factory = ConsoleLoggerFactory()
    factory.log_message("Hello Factory Method")
