import random
import copy
from CGen import *

def mutate(C,L,B,H):  # sourcery skip: merge-comparisons
    '''
    C -> Chromosome
    L,B,H -> Length, Breadth and Height of the bounding frame
    '''
    mutated_C=copy.copy(C)
    for i in range(len(mutated_C)):
        # generating a random value and checking for threshold value
        if random.random()>0.5:
            
            # for colours R,G,B
            if i==0 or i==1 or i==2:
                mutated_C[i]=random.randint(0,255)
            
            #for alpha and roughness factor
            elif i==3 or i==4:
                mutated_C[i]=random.uniform(0,1)
            
            #for vertices and faces
            elif i==5:
                verts=generate_vertices(L,B,H,random.random())
                faces=generate_faces(len(verts),random.random())
                mutated_C[i]=[verts,faces]
    
    return mutated_C


def crossover(C1,C2):
    
    c1=copy.copy(C1)
    c2=copy.copy(C2)
    
    # Choose a random crossover point
    crossover_point = random.randint(0, len(c1))
    
    for i in range(crossover_point,len(c1)):
        c1[i], c2[i] = c2[i], c1[i]
    
    return c1,c2