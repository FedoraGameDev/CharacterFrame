import bpy as blenderpy
from bpy.types import Context, Object, Operator
from typing import List
from ..Debug import Debug
from ..Static import StaticNames, StaticDirs
from ..ErrorHandling.ErrorHandler import ErrorHandler
from ..ErrorHandling.Errors import NotEnoughSelectedException, SelectedTooManyException


class MakeFrame(Operator):
    bl_label = StaticNames.MakeFrameName
    bl_idname = StaticNames.MakeFrameID

    def execute(self, context: Context) -> any:
        ErrorHandler.Try(lambda: self.MakeFrameFromContext(context))
        return {"FINISHED"}

    def MakeFrameFromContext(self, context: Context):
        selectedObject = self.GetSelectedObjectFromSelection(
            context.selected_objects)
        self.MakeFrame(selectedObject)

    def GetSelectedObjectFromSelection(self, selection: List[Object]) -> Object:
        lengthOfSelection: int = len(selection)
        tooManyObjectsSelected: bool = lengthOfSelection > 1
        noObjectSelected: bool = lengthOfSelection == 0

        if tooManyObjectsSelected:
            raise SelectedTooManyException(1)

        if noObjectSelected:
            raise NotEnoughSelectedException(1)

        return selection[0]

    def MakeFrame(self, obj: Object) -> None:
        Debug.Log(obj)
