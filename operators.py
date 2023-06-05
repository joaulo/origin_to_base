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


class JSWK_OT_MoveCenterToBase(bpy.types.Operator):
    bl_idname = "pivot_to_base.move_center_to_base"
    bl_label = "Move center to base"
    bl_description = "Move current center of selected mesh to the middle of bottom vertex"
    bl_options = {'REGISTER', 'UNDO'}
        
    def execute(self, context):
        for o in context.selected_objects:
            if o.type == 'MESH':
                origin_to_bottom(o)
                #origin_to_bottom(o, matrix=o.matrix_world) # global

class JSWK_OT_MoveCenterToBaseV(bpy.types.Operator):
    bl_idname = "pivot_to_base.move_center_to_base_vertices"
    bl_label = "Move center to base (use vertices)"
    bl_description = "Move current center of selected mesh to the middle of bottom vertices"
    bl_options = {'REGISTER', 'UNDO'}
        
    def execute(self, context):
        for o in context.selected_objects:
            if o.type == 'MESH':
                origin_to_bottom(o, use_verts=True)



