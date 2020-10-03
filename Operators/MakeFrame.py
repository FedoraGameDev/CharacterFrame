import bpy as blenderpy
from bpy.types import Context, Object, Operator
from bpy.props import StringProperty
from typing import List
from ..ReturnCodes import FINISHED
from ..Debug import Debug
from ..Static import StaticNames, StaticDirs, ObjectTypes
from ..DataManagement.DataManager import DataManager
from ..ErrorHandling.ErrorHandler import ErrorHandler
from ..ErrorHandling.Errors import NotEnoughSelectedException, SelectedTooManyException, SelectedObjectNotMeshException
from ..DataManagement.SessionMemory import SessionMemory


class MakeFrame(Operator):
    bl_label = StaticNames.MakeFrameName
    bl_idname = StaticNames.MakeFrameID

    frameName: StringProperty(
        name="Frame Name",
        description="Name of the new frame. Defaults to the name of the object."
    )

    @classmethod
    def poll(cls, context: Context):
        lengthCheck = len(context.selected_objects) == 1
        typeCheck = context.object.type in ["MESH"]
        paramCheck = StaticNames.PropObjectType in context.object

        return lengthCheck and typeCheck and not paramCheck

    def invoke(self, context: Context, event):
        self.frameName = context.object.name
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context: Context) -> any:
        ErrorHandler.Try(lambda: self.MakeFrameFromContext(context))
        return FINISHED

    def MakeFrameFromContext(self, context: Context) -> None:
        selectedObject = context.object

        Debug.LogInfo(
            f"['{selectedObject.name}'] {StaticNames.PropObjectType}: '{ObjectTypes.Frame}', {StaticNames.PropFrameName}: {self.frameName}")
        selectedObject[StaticNames.PropObjectType] = ObjectTypes.Frame
        selectedObject[StaticNames.PropFrameName] = self.frameName
