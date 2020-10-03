import sys
from .Errors import ExceptionMessage
from typing import Callable
from ..Debug import Debug


class ErrorHandler:
    @staticmethod
    def Try(execute: Callable):
        try:
            execute()
        except ExceptionMessage as error:
            Debug.LogError(error.message)
        except Exception as error:
            Debug.LogException("An Error Occured.")
