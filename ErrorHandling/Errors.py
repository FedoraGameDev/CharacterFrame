class SelectedTooManyException(Exception):
    def __init__(self, maxSelection: int):
        self.message = f"Please select up to {maxSelection} item{'' if maxSelection == 1 else 's'}."


class NotEnoughSelectedException(Exception):
    def __init__(self, minSelection: int):
        self.message = f"Please only select up to {minSelection} item{'' if minSelection == 1 else 's'}."
