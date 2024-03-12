import bpy
from mathutils import Matrix, Vector
import numpy as np


# without numpy
#def origin_to_bottom(ob, matrix=Matrix()):
#    me = ob.data
#    mw = ob.matrix_world
#    local_verts = [matrix @ Vector(v[:]) for v in ob.bound_box]
#    o = sum(local_verts, Vector()) / 8
#    o.z = min(v.z for v in local_verts)
#    o = matrix.inverted() @ o
#    me.transform(Matrix.Translation(-o))
#
#    mw.translation = mw @ o

# with numpy
def origin_to_bottom(ob, matrix=Matrix(), use_verts=False):
    me = ob.data
    mw = ob.matrix_world
    if use_verts:
        data = (v.co for v in me.vertices)
    else:
        data = (Vector(v) for v in ob.bound_box)


    coords = np.array([matrix @ v for v in data])
    z = coords.T[2]
    mins = np.take(coords, np.where(z == z.min())[0], axis=0)

    o = Vector(np.mean(mins, axis=0))
    o = matrix.inverted() @ o
    me.transform(Matrix.Translation(-o))

    mw.translation = mw @ o


class JSWK_OT_SetOriginToVolumeBase(bpy.types.Operator):
    bl_idname = "pivot_to_base.origin_to_base"
    bl_label = "Move object origin to base (volume base)"
    bl_description = "Move current origin of selected mesh to the middle x,y and lower z of the surrounding volume"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        return bool(context.selected_objects)
    
    def execute(self, context):
        for o in context.selected_objects:
            if o.type == 'MESH':
                origin_to_bottom(o)
                #origin_to_bottom(o, matrix=o.matrix_world) # global
        return {'FINISHED'}

class JSWK_OT_SetOriginToBaseVerts(bpy.types.Operator):
    bl_idname = "pivot_to_base.origin_to_base_vertices"
    bl_label = "Move mesh origin to base (base vertices)"
    bl_description = "Move current origin of selected mesh to the middle of bottom vertices"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        return bool(context.selected_objects)
    
    def execute(self, context):
        for o in context.selected_objects:
            if o.type == 'MESH':
                origin_to_bottom(o, use_verts=True)
        return {'FINISHED'}


classes = (
            JSWK_OT_SetOriginToVolumeBase,
            JSWK_OT_SetOriginToBaseVerts,
           )