import random
import copy
import subprocess

from CGen import *

L,B,H=5,5,8

P1=[]

for _ in range(10):
    CH=generate_chromosome(L,B,H,random.random())
    P1.append(CH)
    get_stats(CH)
    print('-'*125)