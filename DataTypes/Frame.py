from typing import List
from .Point import Point


class Frame:
    def __init__(self, points: List[Point]):
        self.points = points

    def __str__(self) -> str:
        strings = []
        for point in self.points:
            strings.append(str(point))
        string = ", ".join(strings)
        return f"Frame has {len(strings)} Points\n[{string}]"

    def GetPoints(self):
        return self._points

    def SetPoints(self, points: List[Point]):
        self._points = points

    points = property(GetPoints, SetPoints)
