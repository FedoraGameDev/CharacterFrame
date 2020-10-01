import bpy as blenderpy
from bpy.types import Operator, Panel
from ..ReturnCodes import FINISHED
from ..Static import StaticNames


class ConfirmStringOperator(Operator):
    """Set Value"""
    bl_idname = StaticNames.ConfirmStringOpID
    bl_label = StaticNames.ConfirmStringOpName
    bl_options = {"INTERNAL"}

    string: blenderpy.props.StringProperty()

    def execute(self, context):
        self.report({"INFO"}, "YES!")
        return FINISHED

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):
        self.layout.label("Set Value")
        row = self.layout
        row.prop(self, "string", text="Value")
