import bpy as blenderpy
from ..Debug import Debug
from ..Static import StaticNames


class CreateFrame(blenderpy.types.Operator):
    bl_label = StaticNames.CreateFrameName
    bl_idname = StaticNames.CreateFrameID

    def execute(self, context: blenderpy.types.Context) -> any:
        Debug.Log("Creating Frame!")
        return {"FINISHED"}
