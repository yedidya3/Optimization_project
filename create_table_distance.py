import pants
import math
import random
import pandas as pd
import numpy as np
import csv


# Ant colony optimization for TSP
# documentation see here: https://pypi.org/project/ACO-Pants/

def euclidean(a, b):
    return math.sqrt(pow(a[1] - b[1], 2) + pow(a[0] - b[0], 2))

def create_table_from_file(name):
    table_distance = []

    dat = pd.read_csv(name, sep=' ', skiprows=0, names=['nodeId', 'lat', 'lng'])



    for i in range(len(dat)):
        row_distance = []
        
        row1 = dat.loc[[i]]
        x1 = int(row1['lat'])
        y1 = int(row1["lng"])
        a=[x1,y1]
        for i in range(len(dat)):
            row2 = dat.loc[[i]]
            x2 = int(row2['lat'])
            y2 = int(row2["lng"])
            b=[x2,y2]
            row_distance.append(int(euclidean(a,b)))
        table_distance.append(row_distance)
    #print(table_distance)
    return table_distance

    
        
def create_little_table(num , table):
    table2 = []
    table3 = table[:num]
    for row in table3:
        row=row[:num]
        
        table2.append(row)
    return table2
        
def write_csv(name , table ):
    with open(name, "w") as f:
        wr = csv.writer(f)
        wr.writerows(table)
    
    
table = create_table_from_file("./pr1002.tsp")

for i in range (1,500):
    table5 = create_little_table( i,table )
    write_csv("TSPdata"+str(i)+".csv" ,table5)
    
