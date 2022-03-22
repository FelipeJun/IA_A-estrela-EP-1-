from no import No
import heapq
import numpy as np
from map_contructor import *

def a_estrela(estado_inicial, testar_objetivo, gerar_sucessores, heuristica, custo,M , N):
  fila = FilaPrioridade()
  fila.push(No(estado_inicial, None, None, 0.0, heuristica(estado_inicial),0.0))
  saida = [0,[]]
  custo_total = 0

  while not fila.esta_vazio():
    no_atual = fila.pop()
    estado_atual = no_atual.estado
    
    print("\n")
    print(np.reshape(estado_atual, (M, N)))
    if(testar_objetivo(estado_atual,len(estado_atual))):
      return saida
    # verifico os nos filhos e os adiciono na fila
    # função sucessores define os estados seguintes e adiciona os nós seguintes
    estados_vertices_sucessores = gerar_sucessores(estado_atual)
    movimento = None
    for estados_vertices_sucessor in estados_vertices_sucessores:
      no = No(estados_vertices_sucessor[0], no_atual, estados_vertices_sucessor[1],estados_vertices_sucessor[2], heuristica(estados_vertices_sucessor[0]))
      if movimento == None: 
        movimento = no
      else:
        if no.total < movimento.total:
          movimento = no
    custo_total += movimento.custo
    saida[0] = custo_total
    saida[1].append(movimento.vertice)
    fila.push(movimento)
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