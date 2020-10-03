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
        colorCode = COLOR_SEQ % (30 + COLORS[record.levelname])
        levelName = self.CenterBetween(record.levelname, 10)  # , "[", "]")
        message = record.msg
        if record.levelname in COLORS:
            record.levelname = f"[{colorCode}{levelName}{RESET_SEQ}]"
            record.msg = f"{colorCode}{str(message)}{RESET_SEQ}"
        return logging.Formatter.format(self, record)

    def CenterBetween(self, message: str, targetLength: int, before: str = "", after: str = "") -> str:
        if len(message) >= targetLength:
            return f"{before}{message}{after}"
        else:
            if (len(message) % 2 == 0 and targetLength % 2 == 0) or (len(message) % 2 == 1 and targetLength % 2 == 1):
                extra: int = int((targetLength - len(message)) / 2)
                extraSpace: str = " " * extra
                return f"{before}{extraSpace}{message}{extraSpace}{after}"
            else:
                extra: int = int((targetLength - len(message)) / 2)
                extraSpace: str = " " * extra
                return f"{before}{extraSpace}{message} {extraSpace}{after}"
        return f"{before}{message}{after}"


class Debug:
    logger = None

    @staticmethod
    def Init() -> None:
        logLevel = logging.DEBUG
        formatString = '<%(asctime)-15s>%(levelname)s %(message)s'
        formatter = ColoredFormatter(formatString)

        Debug.logger = logging.getLogger(__name__)
        Debug.logger.setLevel(logLevel)

        while len(Debug.logger.handlers) > 0:
            Debug.logger.removeHandler(Debug.logger.handlers[0])

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
    def LogException(message: str) -> None:
        Debug.logger.exception(message)

    @staticmethod
    def LogCritical(message: str) -> None:
        Debug.logger.critical(message)

    @staticmethod
    def LogTest() -> None:
        Debug.Log("Test Log")
        Debug.LogInfo("Test Info")
        Debug.LogWarning("Test Warning")
        Debug.LogError("Test Error")
        Debug.LogCritical("Test Critical")
