import bpy as blenderpy
from bpy.types import Context, Object, Operator
from typing import List
from ..ReturnCodes import FINISHED
from ..Debug import Debug
from ..Static import StaticNames, StaticDirs
from ..DataTypes.Frame import Frame
from ..DataTypes.Point import Point
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

        if lengthOfSelection > 1:
            raise SelectedTooManyException(1)

        if lengthOfSelection == 0:
            raise NotEnoughSelectedException(1)

        selectedObject = selection[0]

        if not selectedObject.type == "MESH":
            raise SelectedObjectNotMeshException()

        return selectedObject

    def MakeFrameFromObject(self, obj: Object) -> None:
        mesh = obj.data
        points: List[Point] = []
        for vertice in mesh.vertices:
            points.append(Point(vertice.co))
        frame = Frame(points)
        Debug.Log(frame)
