import random as rand
import math

def calc_distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

def check_dictionary(dictionary,val):
    if val in dictionary.keys():
        return (dictionary.get(val))
    else:
        return False

def create_map(rows,cols,dictionary):
    map = [([0]*cols) for i in range(rows)]
    key_list = list(dictionary.keys())
    for i in range(rows):
        for j in range(cols):
            map[i][j] = key_list[rand.randrange(0,4)]
    return map

def print_map(map):
    for i in map:
        print(i)

terrains = {'T':1,'A': 3,'Am': 6,'B':-1}
map = create_map(5,7,terrains)

print_map(map)
print(terrains.keys())
print(terrains.values())
print(check_dictionary(terrains,map[0][0]))