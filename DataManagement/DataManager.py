from ..Static import StaticDirs
from ..Debug import Debug
from ..DataTypes.Frame import Frame


class DataManager:
    _localFramesDir = StaticDirs.LocalFrameDatabase
    _localFillerDir = StaticDirs.LocalFillerDatabase

    def SaveFrame(self, frame: Frame, name: str):
        Debug.Log(f"Save Frame '{name}'")

    def LoadFrame(self, name: str):
        Debug.Log(f"Load Frame '{name}'")
