# -*- coding: utf-8 -*-

bl_info = {
    "name": "Text Content Property",
    "author": "listelin",
    "version": (0, 1),
    "blender": (2, 80, 0),
    "location": "Properties Editor > Text > TextContent",
    "description": "Textプロパティにテキスト内容欄を追加し日本語入力可能にします。",     
    "category": "Interface"}

import bpy
from bpy.types import Panel
from bpy.types import TextCurve

class CurveButtonsPanelText:
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        return (type(context.curve) is TextCurve)

class DATA_PT_textcontent(CurveButtonsPanelText, Panel):
    bl_label = "TextContent"

    def draw(self, context):

        text = context.curve
        self.layout.prop(text, "body", text="")       

def register():
    bpy.utils.register_class(DATA_PT_textcontent)

def unregister():
    bpy.utils.unregister_class(DATA_PT_textcontent)

if __name__ == "__main__":
    register()