import os
from pathlib import Path
from ..Packages import jsonpickle
from ..Static import StaticDirs
from ..Debug import Debug
from ..DataTypes.Frame import Frame


class DataManager:
    _localFramesDir = StaticDirs.LocalFrameDatabase
    _localFillerDir = StaticDirs.LocalFillerDatabase

    @staticmethod
    def SaveFrame(frame: Frame, name: str):
        jsonFrame = jsonpickle.encode(frame, indent=4)
        if not DataManager._localFramesDir.exists():
            os.makedirs(DataManager._localFramesDir)

        filename = f"{str(DataManager._localFramesDir)}/{name}"
        num = 0
        while Path(f"{filename}{'' if num == 0 else num}.json").exists():
            num += 1

        finalFileName = f"{filename}{'' if num == 0 else num}"

        with open(f"{finalFileName}.json", "w") as jsonFile:
            jsonFile.write(jsonFrame)

    @staticmethod
    def LoadFrame(name: str):
        Debug.Log(f"Load Frame '{name}'")
