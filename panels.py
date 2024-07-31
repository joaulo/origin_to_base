import bpy

class JSWK_PT_OriginToolsPanel(bpy.types.Panel):
    bl_label = "Origin Tools"
    bl_idname = "VIEW3D_PT_origin_tools"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Origin Tools'
    
    def draw(self, context):
        layout = self.layout
        layout.operator("object.origin_to_base_volume", text="Origin to volume base")
        layout.operator("object.origin_to_base_vertices", text="Origin to bottom vertices")

classes = (
            JSWK_PT_OriginToolsPanel,
           )