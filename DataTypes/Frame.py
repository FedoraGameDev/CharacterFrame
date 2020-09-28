from typing import List
from .Point import Point


class Frame:
    _points: List[Point] = []

    def __init__(self, points: List[Point]):
        _points = points
