class SelectedTooManyException(Exception):
    def __init__(self, maxSelection: int):
        self.message = f"Please select at most {maxSelection} item{'' if maxSelection == 1 else 's'}."


class NotEnoughSelectedException(Exception):
    def __init__(self, minSelection: int):
        self.message = f"Please select at least {minSelection} item{'' if minSelection == 1 else 's'}."


class SelectedObjectNotMeshException(Exception):
    def __init(self):
        self.message = f"The selected object must have mesh data."
