import bpy

class VIEW3D_MT_object_origin_to_base(bpy.types.Menu):
    bl_label = "Origin to Base"
    bl_idname = "VIEW3D_MT_object_origin_to_base"

    def draw(self, context):
        layout = self.layout
        layout.operator("object.origin_to_base_volume", text="Origin to volume base")
        layout.operator("object.origin_to_base_vertices", text="Origin to bottom vertices")

def menu_func(self, context):
    self.layout.separator()
    self.layout.menu(VIEW3D_MT_object_origin_to_base.bl_idname)

def register():
    bpy.utils.register_class(VIEW3D_MT_object_origin_to_base)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.types.VIEW3D_MT_object.remove(menu_func)
    bpy.utils.unregister_class(VIEW3D_MT_object_origin_to_base)
