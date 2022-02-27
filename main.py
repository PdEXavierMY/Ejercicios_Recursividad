import sys
sys.path.insert(1, './ejercicios')
from ejercicios import Bandera, Dicotomia, Palindromos


if __name__ == "__main__":
  inicio = int(input("Elige el ejercicio a realizar(1=Búsqueda por dicotomía,2=Palíndromos,3=Ordenar la bandera): "))
  if inicio == 1 or inicio == 2 or inicio == 3:
    if inicio == 1:
    elif inicio == 2:
      Palindromo().__init__()
    elif inicio == 3:
  else:
    print("Has elegido salir o no has introducido correctamente el número del ejercicio.")