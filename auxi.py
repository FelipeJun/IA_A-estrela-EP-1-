def no_caminho(no):
  caminho = [no.estado]
  while no.no_pai is not None:
    no = no.no_pai
    caminho.append(no.estado)
  caminho.reverse()
  return caminho

def vertice_caminho(no):
  caminho = []
  while no.no_pai is not None:
    no = no.no_pai
    if no.vertice is not None: caminho.append(no.vertice)
  caminho.reverse()
  return caminho
