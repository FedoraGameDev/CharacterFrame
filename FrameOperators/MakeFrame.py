import bpy as blenderpy
from ..Debug import Debug
from ..Static import StaticNames, StaticDirs


class MakeFrame(blenderpy.types.Operator):
    bl_label = StaticNames.MakeFrameName
    bl_idname = StaticNames.MakeFrameID

    def execute(self, context: blenderpy.types.Context):
        objects = context.selected_objects
        if len(objects) > 1:
            Debug.LogError(
                "Too many objects selected. Please ensure only 1 is selected.")
            return {"FINISHED"}

        if len(objects) == 0:
            Debug.LogError("One object must be selected.")
            return {"FINISHED"}

        obj = objects[0]

        self.MakeFrame(obj)

        return {"FINISHED"}

    def MakeFrame(self, obj: blenderpy.types.Object) -> None:
        Debug.Log(obj)
