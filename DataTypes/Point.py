from typing import Tuple

Vector3 = Tuple[float, float, float]


class Point:
    _position: Vector3 = None

    def __init__(self, position: Vector3):
        _position = position
