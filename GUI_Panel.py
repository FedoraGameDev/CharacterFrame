import bpy as blenderpy
from .Debug import Debug

_debug = Debug()


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
        self.layout.label(text="Hello World")


def register():
    _debug.Log("Loading GUI_Panel")


def unregister():
    _debug.Log("Unloading GUI_Panel")
