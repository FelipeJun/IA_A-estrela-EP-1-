class No:
  def __init__(self, estado, no_pai=None, vertice=None, custo=0.0, heuristica=0.0,total=0.0):
    self.estado = estado
    self.no_pai = no_pai
    self.vertice = vertice
    self.custo = custo
    self.heuristica = heuristica
    self.total = self.custo + self.heuristica