import bpy as blenderpy
from .Debug import Debug
from .Static import StaticNames


class GUIPanel(blenderpy.types.Panel):
    bl_label = "Character Frame"
    bl_idname = "OBJECT_PT_character_frame"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Character Frame"

    @classmethod
    def poll(self, context: blenderpy.types.Context) -> bool:
        return context.mode in {"OBJECT", "EDIT_MESH", "PAINT_WEIGHT", "POSE", "VERTEX_PAINT"}

    def draw(self, context) -> None:
        layout = self.layout

        layout.operator(StaticNames.MakeFrameID)
        layout.operator(StaticNames.MakeConnectorID)
        layout.operator(StaticNames.AddConnectorID)


def register() -> None:
    Debug.LogInfo("Loading GUIPanel")


def unregister() -> None:
    Debug.LogInfo("Unloading GUIPanel")
