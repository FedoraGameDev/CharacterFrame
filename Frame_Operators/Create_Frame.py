import bpy as blenderpy
from ..Debug import Debug
from ..Static import StaticNames


class Create_Frame(blenderpy.types.Operator):
    bl_label = StaticNames.CreateFrameName
    bl_idname = StaticNames.CreateFrameID

    def execute(self, context):
        Debug.Log("Creating Frame!")
        return {"FINISHED"}

    def register():
        Debug.Log("Loading Create_Frame")

    def unregister():
        Debug.Log("Unloading Create_Frame")
