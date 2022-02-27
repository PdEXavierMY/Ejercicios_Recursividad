import sys
sys.path.insert(1, './ejercicios')
from ejercicios import O_Bandera, B_Dicotomia, Palindromos

def __init__():
  if __name__ == "__main__":
    inicio = int(input("Elige el ejercicio a realizar(1=Búsqueda por dicotomía,2=Palíndromos,3=Ordenar la bandera): "))
    if inicio == 1 or inicio == 2 or inicio == 3:
      if inicio == 1:
        B_Dicotomia.dicotomia().iniciar()
      elif inicio == 2:
        Palindromos.Palindromo().iniciar()
      elif inicio == 3:
        O_Bandera.bandera().iniciar()
    else:
      print("Has elegido salir o no has introducido correctamente el número del ejercicio.")
__init__()