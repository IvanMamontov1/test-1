class ExternalLogger:
    def logMessage(self, msg: str) -> None:
        print(f"External log: {msg}")


class Logger:
    def log(self, message: str) -> None:
        raise NotImplementedError


class LoggerAdapter(Logger):
    def __init__(self, external_logger: ExternalLogger):
        self._external = external_logger

    def log(self, message: str) -> None:
        self._external.logMessage(message)


if __name__ == "__main__":
    ext = ExternalLogger()
    logger: Logger = LoggerAdapter(ext)
    logger.log("This is a test message.")
