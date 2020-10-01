from typing import Tuple


class Point:
    x: float
    y: float
    z: float

    def __init__(self, position: Tuple[float, float, float]):
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]

    def __str__(self) -> str:
        return f"({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"
