from no import No
import heapq

def a_estrela(estado_inicial, testar_objetivo, gerar_sucessores, heuristica, custo, stepEstado=False, stepSucessores=False):
  fila = FilaPrioridade()
  fila.push(No(estado_inicial, None, None, 0.0, heuristica(estado_inicial)))
  visitados = {estado_inicial: 0.0} # Dicionario do Python

  while not fila.esta_vazio():
    no_atual = fila.pop()
    estado_atual = no_atual.estado

    # faz o teste objetivo conforme a função `teste_objetivo`
    # para a execução se achou o objetivo
    if(testar_objetivo(estado_atual,len(estado_atual))):
      return no_atual
    
    # verifico os nos filhos e os adiciono na fila
    # função sucessores define os estados seguintes e adiciona os nós seguintes
    estados_vertices_sucessores = gerar_sucessores(estado_atual)
    for estados_vertices_sucessor in estados_vertices_sucessores:
      estado_filho = estados_vertices_sucessor[0]
      vertice = estados_vertices_sucessor[1]
      posicao_antiga = estados_vertices_sucessor[2]
      posicao_nova = estados_vertices_sucessor[3]
      novo_custo = no_atual.custo + custo(posicao_antiga, posicao_nova)
      if estado_filho not in visitados or visitados[estado_filho] > novo_custo: # pula estado_filho se já foi expandido
        visitados[estado_filho] = novo_custo
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