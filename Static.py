from pathlib import Path


class StaticDirs:
    RootDirectory = Path(__file__).parent.absolute()
    ResourcesDirectory = Path(f"{str(RootDirectory)}/Resources")
    DefaultFrameDatabase = Path(f"{str(ResourcesDirectory)}/Frames/Default")
    DefaultFillerDatabase = Path(f"{str(ResourcesDirectory)}/Fillers/Default")
    LocalFrameDatabase = Path(f"{str(ResourcesDirectory)}/Frames/Local")
    LocalFillerDatabase = Path(f"{str(ResourcesDirectory)}/Fillers/Local")


class StaticNames:
    Category = "character_frame"
    CreateFrameID = f"{Category}.create_frame"
    CreateFrameName = "New Frame"
    MakeFrameID = f"{Category}.make_frame"
    MakeFrameName = "Make Frame"
