import sys
import bpy
from ast import literal_eval

my_input = sys.argv

FILE_NUM=my_input[4]
COLOUR=literal_eval(my_input[5])

# VERTS=literal_eval(my_input[6])
# FACES=literal_eval(my_input[7])

VERTS_FILE=my_input[6]
FACES_FILE=my_input[7]

RO=int(my_input[8])
OUTPUT_PATH=my_input[9]


    
for obj in bpy.data.objects:
    bpy.data.objects.remove(obj) 

#create mesh and object
mymesh = bpy.data.meshes.new("statue")
myobject = bpy.data.objects.new("statue",mymesh)

#set mesh location
myobject.location = bpy.context.scene.cursor.location
bpy.context.scene.collection.objects.link(myobject)

#create mesh from python data
mymesh.from_pydata(VERTS,[],FACES)
mymesh.update(calc_edges=True)

#set the object to edit mode
bpy.context.view_layer.objects.active = myobject
bpy.ops.object.mode_set(mode='EDIT')

# remove duplicate vertices
bpy.ops.mesh.remove_doubles()

# recalculate normals
bpy.ops.mesh.normals_make_consistent(inside=False)
bpy.ops.object.mode_set(mode='OBJECT')

# subdivide modifier
myobject.modifiers.new("subd", type='SUBSURF')
myobject.modifiers['subd'].levels = RO

# show mesh as smooth
mypolys = mymesh.polygons
for p in mypolys:
    p.use_smooth = True
    
mat = bpy.data.materials.new("MyMaterial")
mat.diffuse_color = COLOUR

myobject.data.materials.append(mat)

bpy.ops.wm.save_as_mainfile(filepath=OUTPUT_PATH+"\\STATUE_"+FILE_NUM+'.blend')
