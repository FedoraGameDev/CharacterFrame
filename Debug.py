import sys
import logging


class Debug:
    logger = None

    @staticmethod
    def Init():
        logLevel = logging.DEBUG
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s')

        Debug.logger = logging.getLogger(__name__)
        Debug.logger.setLevel(logLevel)

        if len(Debug.logger.handlers) <= 1:
            consoleHandler = logging.StreamHandler(sys.stdout)
            consoleHandler.setLevel(logLevel)
            consoleHandler.setFormatter(formatter)
            Debug.logger.addHandler(consoleHandler)

    @staticmethod
    def Log(message: str) -> None:
        Debug.logger.debug(message)

    @staticmethod
    def LogInfo(message: str) -> None:
        Debug.logger.info(message)

    @staticmethod
    def LogWarning(message: str) -> None:
        Debug.logger.warning(message)

    @staticmethod
    def LogError(message: str) -> None:
        Debug.logger.error(message)

    @staticmethod
    def LogCritical(message: str) -> None:
        Debug.logger.critical(message)
