import bpy, bmesh
from mathutils import Vector

objs = bpy.data.objects
if objs.get("Cube"):
    objs.remove(objs["Cube"], do_unlink=True)

file_loc = 'batch_output/texturedMesh.obj'
bpy.ops.import_scene.obj(filepath=file_loc)


def is_inside(vector_check, vector1, vector2):
    for i in range(0, 3):
        if (vector_check[i] < vector1[i] and vector_check[i] < vector2[i]
                or vector_check[i] > vector1[i] and vector_check[i] > vector2[i]):
            return False
    return True


def select_background(object, vector1, vector2):
    mesh = object.data

    if mesh.is_editmode:
        bm = bmesh.from_edit_mesh(mesh)
    else:
        bm = bmesh.new()
        bm.from_mesh(mesh)

    for vert in bm.verts:
        if is_inside(vert.co, vector1, vector2):
            vert.select = False
        else:
            vert.select = True

    if bm.is_wrapped:
        bmesh.update_edit_mesh(mesh)
    else:
        bm.to_mesh(mesh)
        mesh.update()
    bpy.context.view_layer.update()


scene = bpy.context.scene

for obj in scene.objects:
    if obj.type == 'MESH':
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.mode_set(mode='EDIT')
        select_background(obj, Vector((0.4, 0.7, -1.3)), Vector((-0.5, -0.5, -2.1)))
        bpy.ops.mesh.delete(type='VERT')
