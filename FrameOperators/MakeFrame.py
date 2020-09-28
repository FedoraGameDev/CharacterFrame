import bpy as blenderpy
from bpy.types import Context, Object, Operator
from typing import List
from ..Debug import Debug
from ..Static import StaticNames, StaticDirs


class MakeFrame(Operator):
    bl_label = StaticNames.MakeFrameName
    bl_idname = StaticNames.MakeFrameID

    def execute(self, context: Context) -> any:
        allSelectedObjects: List[Object] = context.selected_objects
        lengthOfSelectedObjects: int = len(allSelectedObjects)
        tooManyObjectsSelected: bool = lengthOfSelectedObjects > 1
        noObjectSelected: bool = lengthOfSelectedObjects == 0

        if tooManyObjectsSelected:
            Debug.LogError("Please ensure only 1 object is selected.")
            return {"FINISHED"}

        if noObjectSelected:
            Debug.LogError("One object must be selected.")
            return {"FINISHED"}

        selectedObject: Object = allSelectedObjects[0]

        self.MakeFrame(selectedObject)

        return {"FINISHED"}

    def MakeFrame(self, obj: Object) -> None:
        Debug.Log(obj)
