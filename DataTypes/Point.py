from typing import Tuple

Vector3 = Tuple[float, float, float]


class Point:
    def __init__(self, position: Vector3):
        self.position = position

    def __str__(self) -> str:
        return f"({self._position[0]:.2f},{self._position[1]:.2f},{self._position[2]:.2f})"

    def GetPosition(self) -> Vector3:
        return self._position

    def SetPosition(self, position: Vector3) -> None:
        self._position = position

    position = property(GetPosition, SetPosition)
