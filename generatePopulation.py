import sys
import bpy

my_input = sys.argv

FILE_NUM=my_input[4]
HEX_VALUE=my_input[5]
VERTS=my_input[6]
FACES=my_input[7]
RO=my_input[8]


    
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
mat.diffuse_color = HEX_VALUE

myobject.data.materials.append(mat)

FILE_SAVE_PATH="E:\\Research\\Statue Generator\\Rough Work\\Test\\"
bpy.ops.wm.save_as_mainfile(filepath=FILE_SAVE_PATH+"STATUE_"+FILE_NUM+'.blend')
