import bpy as blenderpy
from .Debug import Debug
from .Static import StaticNames


class GUI_Panel(blenderpy.types.Panel):
    bl_label = "Character Frame"
    bl_idname = "OBJECT_PT_character_frame"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Character Frame"

    @classmethod
    def poll(cls, context):
        return context.mode in {"OBJECT", "EDIT_MESH", "PAINT_WEIGHT", "POSE"}

    def draw(self, context):
        layout = self.layout

        layout.operator(StaticNames.CreateFrameID)


class Create_Frame(blenderpy.types.Operator):
    bl_label = StaticNames.CreateFrameName
    bl_idname = StaticNames.CreateFrameID

    def execute(self, context):
        Debug.Log("Creating Frame!")
        return {"FINISHED"}


def register():
    Debug.Log("Loading GUI_Panel")


def unregister():
    Debug.Log("Unloading GUI_Panel")
