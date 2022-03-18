import random as rand
import math
from map_contructor import *

terrains = {'T':1,'A': 3,'Am': 6,'B':-1}
map = create_map(5,7,terrains)
map_values = create_map_values(5,7,terrains)
print_map(map)
print_map(map_values)
print(map_values[0][0])