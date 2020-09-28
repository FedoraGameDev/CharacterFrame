from typing import Callable
from ..Debug import Debug


class ErrorHandler:
    @staticmethod
    def Try(execute: Callable):
        try:
            execute()
        except Exception as error:
            Debug.LogError(error.message)
