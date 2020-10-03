import os
from pathlib import Path
from ..Packages import jsonpickle
from ..Static import StaticDirs
from ..Debug import Debug


class DataManager:
    _localFramesDir = StaticDirs.LocalFrameDatabase
    _localFillerDir = StaticDirs.LocalFillerDatabase

    @staticmethod
    def LoadFrame(name: str):
        Debug.Log(f"Load Frame '{name}'")
