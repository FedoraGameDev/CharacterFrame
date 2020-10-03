import bpy as blenderpy
from bpy.types import Context, Operator
from ..Static import StaticNames, ObjectTypes


class AddConnector(Operator):
    bl_label = StaticNames.AddConnectorName
    bl_idname = StaticNames.AddConnectorID

    @classmethod
    def poll(cls, context: Context):
        correctSelected: bool = len(context.selected_objects) == 2
        if not correctSelected:
            return False

        firstObject = context.object
        secondObject = context.selected_objects[1]

        if StaticNames.PropObjectType in firstObject:
            if StaticNames.PropObjectType in secondObject:
                if firstObject.get(StaticNames.PropObjectType) == ObjectTypes.Frame:
                    return secondObject.get(StaticNames.PropObjectType) == ObjectTypes.Connector
        return False
