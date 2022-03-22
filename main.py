from cmath import sqrt
import random as rand
from map_contructor import *
import numpy as np
from a_estrela import a_estrela

class Jogo:

    def testar_objetivo(self,map,array_size):
        return map[array_size - 1] == 0

    def gerar_sucessores(self, estado):
        sucessores = []

        posicao = estado.index(0)
        expansoes = [self._direita, self._esquerda, self._cima, self._baixo]
        rand.shuffle(expansoes)
        for expansao in expansoes:
            sucessor = expansao(posicao, estado)
            if sucessor is not None: sucessores.append(sucessor)

        return sucessores

    def _esquerda(self, posicao, estado_atual):
        esquerda = []
        for i in range(len(map)):
            if i == 0 or i % N == 0:
                esquerda.append(i)
        if posicao not in esquerda and 0 < estado_atual[posicao-1]:
            sucessor = list(estado_atual)
            sucessor[posicao] = -2
            sucessor[posicao - 1] = 0
            return (tuple(sucessor), "⬅️",estado_atual[(posicao - 1)])

    def _cima(self, posicao, estado_atual):
        cima = []
        for i in range(len(map)):
            if 0 <= i < N:
                cima.append(i)
        if posicao not in cima and 0 < estado_atual[posicao-N]:
            sucesso = list(estado_atual)
            sucesso[posicao] = -2
            sucesso[posicao - N] = 0
            return (tuple(sucesso), "⬆️",estado_atual[(posicao - N)])

    def _baixo(self, posicao, estado_atual):
        baixo = []
        for i in range(len(map)):
            if len(map) % 2 == 0:
                if i >= (M * N) - M:
                    baixo.append(i)
            else:
                if i >= (M * N) - N:
                    baixo.append(i)
        if posicao not in baixo and 0 < estado_atual[posicao+M]:
            sucessor = list(estado_atual)
            sucessor[posicao] = -2
            sucessor[posicao + M] = 0
            return (tuple(sucessor), "⬇️",estado_atual[(posicao + M)])

    def _direita(self, posicao, estado_atual):
        direita = []
        for i in range(len(map)):
            if (i + 1) % N == 0 :
                direita.append(i)
        if posicao not in direita and 0 < estado_atual[posicao + 1]:      
            sucessor = list(estado_atual)
            sucessor[posicao] = -2
            sucessor[posicao + 1] = 0
            return (tuple(sucessor), "➡️",estado_atual[(posicao + 1)])

    # def _cima_direita(self, posicao, estado_atual):
    #     direita = []
    #     for i in range(len(map)):
    #         if (i + 1) % N == 0 :
    #             direita.append(i)
    #     cima = []
    #     for i in range(len(map)):
    #         if 0 <= i < N:
    #             cima.append(i)
    #     if (posicao not in cima and posicao not in direita) and 0 < estado_atual[posicao - (N - 1)] :
    #         sucessor = list(estado_atual)
    #         sucessor[posicao] = -2
    #         sucessor[posicao - (N - 1)] = 0
    #         return (tuple(sucessor), "Cima-direita",estado_atual[posicao - (N - 1)])
    # def _cima_esquerda(self, posicao, estado_atual):
    #     cima = []
    #     for i in range(len(map)):
    #         if 0 <= i < N:
    #             cima.append(i)
    #     esquerda = []
    #     for i in range(len(map)):
    #         if i == 0 or i % N == 0:
    #             esquerda.append(i)
    #     if (posicao not in cima and posicao not in esquerda) and 0 < estado_atual[posicao - (N + 1)]:
    #         sucessor = list(estado_atual)
    #         sucessor[posicao] = -2
    #         sucessor[posicao - (N + 1)] = 0
    #         return (tuple(sucessor), "Cima-Esquerda",estado_atual[posicao - (N + 1)])

    def manhattan(self, estado):
        map_matrix = np.reshape(estado, (M, N))
        x = 0
        y = 0
        for i in range(len(map_matrix)):
            for j in range(len(map_matrix[i])):
                if map_matrix[i][j] == 0:
                    x = i
                    y = j
                    return self.distancia_manhattan(x,y)

    # Distância de Manhattan: d = |xi-xj| + |yi-yj|
    #                             |xi-M-1| + |yi-N-1|
    def distancia_manhattan(self,i, j):
        return abs(i-(M - 1))+abs(j-(N - 1))
    
    # def euclidiana(self,estado):
    #     map_matrix = np.reshape(estado, (M, N))
    #     x = 0
    #     y = 0
    #     for i in range(len(map_matrix)):
    #         for j in range(len(map_matrix[i])):
    #             if map_matrix[i][j] == 0:
    #                 x = i
    #                 y = j
    #     return self.distancia_euclidiana(x,y)

    # def distancia_euclidiana(self,i, j):
    #     return sqrt((i - (M-1))**2 + (j - (N - 1)**2))

    def custo(self, estado_origem, estado_destino):
        return estado_origem + estado_destino

if __name__ == "__main__":
    g = Jogo()
    terrains = {'T':1,'A': 3,'Am': 6,'B':-1}
    M = int(input("Digite o valor para matriz quadrada: "))
    N = M
    array_size = M * N
    map = create_map(array_size,terrains)
    map_values = tuple(create_map_values(array_size,terrains,map))
    map_matrix = np.reshape(map, (M, N))
    map_matrixValues = np.reshape(map_values, (M, N))
    print(map_matrix)
    Manhattan = a_estrela(map_values, 
                            g.testar_objetivo, 
                            g.gerar_sucessores, 
                            g.manhattan,
                            g.custo,
                            M,
                            N)

    # euclidiana = a_estrela(map_values, 
    #                         g.testar_objetivo, 
    #                         g.gerar_sucessores, 
    #                         g.euclidiana,
    #                         g.custo)

    if(Manhattan is None):
        print("Não houve solução ao problema")
    else:
        print("Solução:")
        # print(vertice_caminho(Manhattan))
        print("Custo total dos terrenos: " + str(Manhattan[0]))
        print("Vértices: " + str(Manhattan[1]))