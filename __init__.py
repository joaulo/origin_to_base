# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


from . import operators, panels, menus
import bpy

bl_info = {
    "name" : "origin_to_base",
    "author" : "joaulo <jsoftworks@joaulo.com>",
    "description" : "Move mesh origin to the center bottom",
    "blender" : (2, 80, 0),
    "version" : (1, 2, 0),
    "location" : "",
    "category" : "Mesh",
    # "warning": "",  # used for warning icon and text in addons panel
    "doc_url" : "https://github.com/joaulo/pivot_to_base",
    # "tracker_url": "",
}

classes = operators.classes + panels.classes

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    menus.register()

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    menus.unregister()

if __name__ == "__main__":
    register()