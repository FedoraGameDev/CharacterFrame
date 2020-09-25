from pathlib import Path


class StaticDirs:
    RootDirectory = Path(__file__).parent.absolute()
    ResourcesDirectory = Path(RootDirectory.__str__() + "/Resources")
    LocalFrameDatabase = Path(ResourcesDirectory.__str__() + "/Frames")
    LocalPartDatabase = Path(ResourcesDirectory.__str__() + "/Parts")


class StaticNames:
    Category = "character_frame"
    CreateFrameID = f"{Category}.create_frame"
    CreateFrameName = "New Frame"
