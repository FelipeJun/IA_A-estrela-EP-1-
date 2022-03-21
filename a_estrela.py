from no import No
import heapq
import numpy as np
from map_contructor import *

def a_estrela(estado_inicial, testar_objetivo, gerar_sucessores, heuristica, custo, stepEstado=False, stepSucessores=False):
  fila = FilaPrioridade()
  fila.push(No(estado_inicial, None, None, 0.0, heuristica(estado_inicial),0.0))

  while not fila.esta_vazio():
    no_atual = fila.pop()
    estado_atual = no_atual.estado
    # faz o teste objetivo conforme a função teste_objetivo
    # para a execução se achou o objetivo
    if(testar_objetivo(estado_atual,len(estado_atual))):
      return no_atual

    print("\n")
    print(np.reshape(estado_atual, (4, 4)))
    print("\n")
    # verifico os nos filhos e os adiciono na fila
    # função sucessores define os estados seguintes e adiciona os nós seguintes
    estados_vertices_sucessores = gerar_sucessores(estado_atual)
    movimento = None
    for estados_vertices_sucessor in estados_vertices_sucessores:
      if movimento == None: 
        movimento = No(estados_vertices_sucessores[0], estado_atual, estados_vertices_sucessores[1],estados_vertices_sucessores[3], heuristica(estado_inicial))
      else:
        if estados_vertices_sucessor.total < movimento.total:

    fila.push(No(estado_filho, no_atual, vertice, novo_custo, heuristica(estado_filho)))
  return None

class FilaPrioridade:
  def __init__(self):
    self.fila = []
  
  def push(self, item):
    heapq.heappush(self.fila, item)
  
  def pop(self):
    if(self.esta_vazio()):
        return None
    else:
        return heapq.heappop(self.fila)

  def esta_vazio(self):
    return len(self.fila) == 0