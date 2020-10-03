import bpy as blenderpy
from bpy.types import Context, Operator
from bpy.props import StringProperty
from ..Debug import Debug
from ..Static import StaticNames, ObjectTypes
from ..ReturnCodes import FINISHED
from ..ErrorHandling.ErrorHandler import ErrorHandler


class MakeConnector(Operator):
    bl_label = StaticNames.MakeConnectorName
    bl_idname = StaticNames.MakeConnectorID

    connectorName: StringProperty(
        name="Connector Name",
        description="Name of the new connector. Defaults to the object's name."
    )

    @classmethod
    def poll(cls, context: Context) -> bool:
        lengthCheck = len(context.selected_objects) == 1
        typeCheck = context.object.type in ["MESH"]
        paramCheck = StaticNames.PropObjectType in context.object

        return lengthCheck and typeCheck and not paramCheck

    def invoke(self, context: Context, event):
        self.connectorName = context.object.name
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context: Context):
        ErrorHandler.Try(lambda: self.MakeConnectorFromContext(context))
        return FINISHED

    def MakeConnectorFromContext(self, context: Context):
        selectedObject = context.object

        Debug.LogInfo(
            f"['{selectedObject.name}'] {StaticNames.PropObjectType}: '{ObjectTypes.Connector}', {StaticNames.PropConnectorName}: {self.connectorName}")
        selectedObject[StaticNames.PropObjectType] = ObjectTypes.Connector
        selectedObject[StaticNames.PropConnectorName] = self.connectorName
