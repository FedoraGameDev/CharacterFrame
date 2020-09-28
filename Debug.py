import sys
import logging

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)
RESET_SEQ = "\033[0m"
COLOR_SEQ = "\033[1;%dm"
COLORS = {
    "WARNING": YELLOW,
    "INFO": GREEN,
    "DEBUG": BLUE,
    "CRITICAL": MAGENTA,
    "ERROR": RED
}


class ColoredFormatter(logging.Formatter):
    def format(self, record):
        levelName = record.levelname
        message = record.msg
        if levelName in COLORS:
            record.levelname = COLOR_SEQ % (
                30 + COLORS[levelName]) + levelName + RESET_SEQ
            record.msg = COLOR_SEQ % (
                30 + COLORS[levelName]) + str(message) + RESET_SEQ
        return logging.Formatter.format(self, record)


class Debug:
    logger = None

    @staticmethod
    def Init() -> None:
        logLevel = logging.DEBUG
        formatter = ColoredFormatter(
            '[%(levelname)-19s] - %(message)s')

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
