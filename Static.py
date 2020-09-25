from pathlib import Path

__all__ = (
    "RootDirectory",
    "ResourcesDirectory",
    "LocalFrameDatabase",
    "LocalPartDatabase"
)


RootDirectory = Path(__file__).parent.absolute()
ResourcesDirectory = Path(RootDirectory.__str__() + "/Resources")
LocalFrameDatabase = Path(ResourcesDirectory.__str__() + "/Frames")
LocalPartDatabase = Path(ResourcesDirectory.__str__() + "/Parts")
