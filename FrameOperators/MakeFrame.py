import bpy as blenderpy
from bpy.types import Context, Object, Operator
from bpy.props import StringProperty
from typing import List
from ..ReturnCodes import FINISHED
from ..Debug import Debug
from ..Static import StaticNames, StaticDirs
from ..DataManagement.DataManager import DataManager
from ..ErrorHandling.ErrorHandler import ErrorHandler
from ..ErrorHandling.Errors import NotEnoughSelectedException, SelectedTooManyException, SelectedObjectNotMeshException
from ..DataManagement.SessionMemory import SessionMemory


class MakeFrame(Operator):
    bl_label = StaticNames.MakeFrameName
    bl_idname = StaticNames.MakeFrameID

    filename: StringProperty(
        name="Frame Name",
        description="Name of the new frame. Defaults to the name of the object."
    )

    @classmethod
    def poll(cls, context):
        selectedLength = len(context.selected_objects)
        return selectedLength == 1 and context.selected_objects[0].type in ["MESH"]

    def invoke(self, context, event):
        self.filename = context.selected_objects[0].name
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context: Context) -> any:
        ErrorHandler.Try(lambda: self.TurnObjectIntoFrame(context))
        return FINISHED

    def TurnObjectIntoFrame(self, context: Context) -> None:
        selectedObject = context.selected_objects[0]

        selectedObject["CF_ObjectType"] = "Frame"
        selectedObject["CF_FrameName"] = self.filename
