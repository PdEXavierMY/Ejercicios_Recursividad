import itertools
class bandera():
  def extraercolores(self, n, fichas, color1, color2, color3):
    if n <= (len(fichas)-1):
      if fichas[n] == "R":
        color1.append("R")
      elif fichas[n] == "A":
        color2.append("A")
      elif fichas[n] == "V":
        color3.append("V")
      bandera().extraercolores(n+1, fichas, color1, color2, color3)

  def iniciar(self):
    self.bandera_caotica = ["R", "A", "A", "R", "V", "A", "A", "R", "A", "R", "R", "V", "R", "R", "A", "V", "V"] #Cadena ya separada(de ser introducida tipo [RAARVAA...] simplemente se le pasaría un split)
    self.color1 = []
    self.color2 = []
    self.color3 = []#partimos de conocer los n colores, aunque la cantidad de fichas puede variar
    bandera().extraercolores(0, self.bandera_caotica, self.color1, self.color2, self.color3)
    bandera_ordenada = list(itertools.chain(self.color1, self.color3, self.color2))
    print("La bandera con los colores agrupados queda de la siguiente forma: " + str(bandera_ordenada))