import pants
import math
import random
import pandas as pd
from numpy import genfromtxt
import sys

import tracemalloc

import time




path = sys.argv[1]




my_data = genfromtxt(path, delimiter=',')
nodes = list(range(len(my_data)))


def euclidean(a, b):   
    v= my_data[a][b]   
    return v

world = pants.World(nodes, euclidean)
Ant1 = 3   
solver = pants.Solver(ant_count = Ant1 , limit=3)



# Driver Cde
tracemalloc.start()
start_time = time.time()


solution = solver.solve(world)



f = open("memory_ACO_TSP.txt", "a")
f.write(str(len(solution.tour))+": " + str(tracemalloc.get_traced_memory()[1])+"\n" )
f.close()


tracemalloc.stop()   
t =time.time() - start_time
print("--- %s seconds ---" % (t)) 
f = open("time_ACO_TSP.txt", "a")
f.write(str(len(solution.tour))+": " + str(t)+"\n" )
f.close()

f = open("length_path_ACO_TSP.txt", "a")
f.write(str(len(solution.tour))+": " + str(solution.distance)+"\n" )
f.close()




print("solution.distance:  " ,solution.distance)
#Ant1+=5
print("solution.tour:  ",solution.tour)    # Nodes visited in order
    #print("solution.path:  ",solution.path)    # Edges taken in order
#print(d.__dict__)


