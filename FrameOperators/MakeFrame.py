import bpy as blenderpy
from bpy.types import Context, Object, Operator
from typing import List
from ..ReturnCodes import FINISHED
from ..Debug import Debug
from ..Static import StaticNames, StaticDirs
from ..DataTypes.Frame import Frame
from ..DataManagement.DataManager import DataManager
from ..ErrorHandling.ErrorHandler import ErrorHandler
from ..ErrorHandling.Errors import NotEnoughSelectedException, SelectedTooManyException, SelectedObjectNotMeshException


class MakeFrame(Operator):
    bl_label = StaticNames.MakeFrameName
    bl_idname = StaticNames.MakeFrameID

    def execute(self, context: Context) -> any:
        ErrorHandler.Try(lambda: self.MakeFrameFromContext(context))
        return FINISHED

    def MakeFrameFromContext(self, context: Context):
        selectedObject = self.GetSelectedObjectFromSelection(
            context.selected_objects)
        self.MakeFrameFromObject(selectedObject)

    def GetSelectedObjectFromSelection(self, selection: List[Object]) -> Object:
        lengthOfSelection: int = len(selection)
        tooManyObjectsSelected: bool = lengthOfSelection > 1
        noObjectSelected: bool = lengthOfSelection == 0

        if tooManyObjectsSelected:
            raise SelectedTooManyException(1)

        if noObjectSelected:
            raise NotEnoughSelectedException(1)

        selectedObject = selection[0]
        selectedObjectTypeIsMesh = selectedObject.type == "MESH"

        if not selectedObjectTypeIsMesh:
            raise SelectedObjectNotMeshException()

        return selectedObject

    def MakeFrameFromObject(self, obj: Object) -> None:
        mesh = obj.data
        Debug.Log(mesh)
