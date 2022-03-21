import random as rand
import math
from map_contructor import *
import numpy as np
from a_estrela import a_estrela

class Jogo:

    def testar_objetivo(self,map,array_size):
        return map[array_size - 1] == 0

    # Função que gera os sucessores válidos 
    # a partir de um estado válido
    def gerar_sucessores(self, estado):
        sucessores = []

        # encontra a posição do _
        posicao = estado.index(0)
        print(posicao)

        expansoes = [self._direita, self._esquerda, self._cima, self._baixo]
        #rand.shuffle(expansoes)
        for expansao in expansoes:
            sucessor = expansao(posicao, estado)
            if sucessor is not None: sucessores.append(sucessor)

        return sucessores

    def _esquerda(self, posicao, estado_atual):
        esquerda = []
        esquerda_values = []
        for i in range(len(map)):
            #esquerda
            if i == 0 or i % N == 0:
                esquerda.append(i)
                esquerda_values.append(estado_atual[i])
        if posicao not in esquerda and 0 < estado_atual[posicao-1]:
            # peça de baixo desce
            sucessor = list(estado_atual)
            sucessor[posicao] = -2
            sucessor[posicao - 1] = 0
            return (tuple(sucessor), "⬅️",posicao,estado_atual[(posicao - 1)])

    def _cima(self, posicao, estado_atual):
        # movimento para cima
        ## Não gera se estiver no topo
        cima = []
        cima_values = []
        for i in range(len(map)):
            #cima
            if 0 <= i < N:
                cima.append(i)
                cima_values.append(estado_atual[i])
        if posicao not in cima and 0 < estado_atual[posicao-N]:
            # peça de baixo sobe
            sucesso = list(estado_atual)
            sucesso[posicao] = -2
            sucesso[posicao - N] = 0
            return (tuple(sucesso), "⬆️",posicao,estado_atual[(posicao - N)])

    def _baixo(self, posicao, estado_atual):
        # movimento para baixo
        ## Não gera se estiver no fundo
        baixo = []
        baixo_values = []
        for i in range(len(map)):
            #baixo
            if len(map) % 2 == 0:
                if i >= (M * N) - M:
                    baixo.append(i)
                    baixo_values.append(estado_atual[i])
            else:
                if i >= (M * N) - N:
                    baixo.append(i)
                    baixo_values.append(estado_atual[i])
        if posicao not in baixo and 0 < estado_atual[posicao+M]:
            # peça de baixo desce
            sucessor = list(estado_atual)
            sucessor[posicao] = -2
            sucessor[posicao + M] = 0
            return (tuple(sucessor), "⬇️",posicao,estado_atual[(posicao + M)])

    def _direita(self, posicao, estado_atual):
    # movimento para direita
    ## Não gera se estiver na direita
        direita = []
        direita_values = []
        for i in range(len(map)):
            #direita
            if (i + 1) % N == 0 :
                direita.append(i)
                direita_values.append(estado_atual[i])
        if posicao not in direita and 0 < estado_atual[posicao+1]:
            # peça de baixo desce
            sucessor = list(estado_atual)
            sucessor[posicao] = -2
            sucessor[posicao + 1] = 0
            return (tuple(sucessor), "➡️",posicao,estado_atual[(posicao + 1)])

    # Heurística 2: Distância para o resultado espero
    # Heurística adminissível, pois, sempre o resultado chega mais perto
    # Transformei o array em matriz para fazer cálculo de distância
    def heuristica2(self, estado):
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
        
    # Função de custo: Quando custa mover de um 
    # estado_origem para estado_destino. No Quebra Cabeça 
    # de 8, este custo é fixo e arbitrariamente será 1.
    def custo(self, estado_origem, estado_destino):
        return estado_origem + estado_destino



if __name__ == "__main__":
    g = Jogo()
    terrains = {'T':1,'A': 3,'Am': 6,'B':-1}
    M = int(input("Digite o valor para M: "))
    N = int(input("Digite o valor para N: "))
    array_size = M * N
    map = create_map(array_size,terrains)
    map_values = tuple(create_map_values(array_size,terrains,map))
    mapa = tuple([0,3,3,-1,-1,1,6,6,-1,-1,3,6, 6,1,1,3])
    map_matrix = np.reshape(map, (M, N))
    map_matrixValues = np.reshape(mapa, (M, N))
    print(map_matrix)
    print(map_matrixValues)
    no_solucao = a_estrela(mapa, 
                            g.testar_objetivo, 
                            g.gerar_sucessores, 
                            g.heuristica2,
                            g.custo)
    print(no_solucao)

    if(no_solucao is None):
        print("Não houve solução ao problema")
    else:
        print("Solução:")
        caminho = vertice_caminho(no_solucao)
        print(caminho)