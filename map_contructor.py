import random as rand
import math

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

def create_map_values(rows,cols,dictionary):
    map = [([0]*cols) for i in range(rows)]
    values_list = list(dictionary.values())
    for i in range(rows):
        for j in range(cols):
            map[i][j] = values_list[rand.randrange(0,4)]
    return map


def print_map(map):
    for i in map:
        print(i)