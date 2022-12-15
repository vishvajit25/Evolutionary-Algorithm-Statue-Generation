import random
import copy
import subprocess
import bpy

from CGen import *

L,B,H=5,5,8

P1=[]

for _ in range(2):
    CH=generate_chromosome(L,B,H,random.random())
    P1.append(CH)
    get_stats(CH)
    print('-'*125)



for i,C in enumerate(P1):
    R,G,B,A=C[0],C[1],C[2],C[3]
    HEX_VALUE="#{:02x}{:02x}{:02x}{:02x}".format(R,G,B,A)
    
    for obj in bpy.data.objects:
        bpy.data.objects.remove(obj) 
    
    #create mesh and object
    mymesh = bpy.data.meshes.new("statue")
    myobject = bpy.data.objects.new("statue",mymesh)
    
    #set mesh location
    myobject.location = bpy.context.scene.cursor.location
    bpy.context.scene.collection.objects.link(myobject)
    
    #create mesh from python data
    mymesh.from_pydata(C[5][0],[],C[5][1])
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
    myobject.modifiers['subd'].levels = C[4]
    
    # show mesh as smooth
    mypolys = mymesh.polygons
    for p in mypolys:
        p.use_smooth = True
        
    mat = bpy.data.materials.new("MyMaterial")
    mat.diffuse_color = HEX_VALUE

    myobject.data.materials.append(mat)
    
    FILE_SAVE_PATH="E:\\Research\\Statue Generator\\Rough Work\\Test\\"
    bpy.ops.wm.save_as_mainfile(filepath=FILE_SAVE_PATH+"STATUE_"+FILE_NUM+'.blend')
