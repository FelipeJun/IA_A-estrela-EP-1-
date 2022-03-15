import random as rand

terrenos = [('T',1),('A',3),('Am',6),('B',-1)]
terrenos_dic = dict(terrenos)
rows, cols = 3,3
mapa = [None] * (rows * cols)
# print(mapa)
# print(terrenos_dic)
# print(terrenos_dic.keys())
for i in range(rows * cols):
    mapa[i] = terrenos[rand.randrange(0,4)][0]
print(mapa)