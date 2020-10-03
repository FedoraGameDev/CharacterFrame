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
    MakeFrameID = f"{Category}.make_frame"
    MakeFrameName = "Make Frame"
    AddConnectorID = f"{Category}.add_connector"
    AddConnectorName = "Add Connector"
    MakeConnectorID = f"{Category}.make_connector"
    MakeConnectorName = "Make Connector"

    PropPrefix = "CF_"
    PropFramePrefix = "Frame_"
    PropConnectorPrefix = "Connector_"
    PropObjectType = f"{PropPrefix}ObjectType"
    PropFrameName = f"{PropPrefix}{PropFramePrefix}Name"
    PropConnectorName = f"{PropPrefix}{PropConnectorPrefix}Name"


class ObjectTypes:
    Frame = "Frame"
    Connector = "Connector"
