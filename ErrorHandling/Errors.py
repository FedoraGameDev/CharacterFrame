class ExceptionMessage(Exception):
    message: str = ""

    def __init__(self, message):
        self.message = message


class SelectedTooManyException(ExceptionMessage):
    def __init__(self, maxSelection: int):
        self.message = f"Please select at most {maxSelection} item{'' if maxSelection == 1 else 's'}."


class NotEnoughSelectedException(ExceptionMessage):
    def __init__(self, minSelection: int):
        self.message = f"Please select at least {minSelection} item{'' if minSelection == 1 else 's'}."


class SelectedObjectNotMeshException(ExceptionMessage):
    def __init(self):
        self.message = f"The selected object must have mesh data."
