import sys
sys.path.insert(1, './ejercicios')
from ejercicios import Bandera, B_Dicotomia, Palindromos

def __init__(self):
  if __name__ == "__main__":
    self.inicio = int(input("Elige el ejercicio a realizar(1=Búsqueda por dicotomía,2=Palíndromos,3=Ordenar la bandera): "))
    if self.inicio == 1 or self.inicio == 2 or self.inicio == 3:
      if self.inicio == 1:
        B_Dicotomia.dicotomia().iniciar()
      elif self.inicio == 2:
        Palindromos.Palindromo().iniciar()
      elif self.inicio == 3:
        Bandera.bandera().iniciar()
    else:
      print("Has elegido salir o no has introducido correctamente el número del ejercicio.")
__init__()