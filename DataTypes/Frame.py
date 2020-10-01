from typing import List
from .Point import Point


class Frame:
    points: List[Point]

    def __init__(self, points: List[Point]):
        self.points = points

    def __str__(self) -> str:
        strings = []
        for point in self.points:
            strings.append(str(point))
        string = ", ".join(strings)
        return f"Frame has {len(strings)} Points\n[{string}]"
