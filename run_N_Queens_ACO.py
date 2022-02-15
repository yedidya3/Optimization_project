# -*- coding: utf-8 -*-
"""
@author: ofersh@telhai.ac.il
"""
from ACO import AntforTSP as ACO
import numpy as np
import os
import tracemalloc
import sys


if __name__ == "__main__" :
    n_queens = int(sys.argv[1])
    
    for k in range(15):
        Niter = 500
        Nant = 200
        
        ant_colony = ACO(n_queens,Nant, Niter, rho=0.95, alpha=1, beta=10)
        
        shortest_path = ant_colony.run()
        
    
        
        # for i in range(n_queens):
        #     for j in range(n_queens):
        #         if shortest_path[0][i] == j:
        #             print(1, end='')
        #         else:
        #             print(0, end='')
        #         print(" ", end='')
        #     print()
        # print("shotest_path: {}".format(shortest_path))
    