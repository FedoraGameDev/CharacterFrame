import sys
import logging

__all__ = ("Debug")


class Debug:
    class __Singleton:
        logger = None

        def __init__(self):
            logLevel = logging.DEBUG
            formatter = logging.Formatter(
                '%(asctime)s - %(levelname)s - %(message)s')

            consoleHandler = logging.StreamHandler(sys.stdout)
            consoleHandler.setLevel(logLevel)
            consoleHandler.setFormatter(formatter)

            self.logger = logging.getLogger(__name__)
            self.logger.setLevel(logLevel)
            self.logger.addHandler(consoleHandler)

    instance = None

    def __init__(self):
        if not Debug.instance:
            Debug.instance = Debug.__Singleton()

    def Log(self, message: str) -> None:
        Debug.instance.logger.debug(message)

    def LogInfo(self, message: str) -> None:
        Debug.instance.logger.info(message)

    def LogWarning(self, message: str) -> None:
        Debug.instance.logger.warning(message)

    def LogError(self, message: str) -> None:
        Debug.instance.logger.error(message)

    def LogCritical(self, message: str) -> None:
        Debug.instance.logger.critical(message)
