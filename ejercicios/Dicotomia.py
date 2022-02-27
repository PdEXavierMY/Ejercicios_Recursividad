class dicotomia():
  tabla = ["cantar", "estupefacto", "incrédulo", "casa", "perro", "dormir", "leer", "planta", "libro", "soñar", "Word", "carrera", "disfrutar", "Qué?", "odio", "vida", "juega", "suspender", "aprobado", "decepción", "descanso", "alegría", "No", "manchar", "actitud", "Pedro", "hoy", "baúl", "bailar", "seis", "más", "palabras", "casi", "llegar", "negro"]
  tabla_ord = sorted(tabla)
  print(tabla_ord)
  palabra = str(input("Introduce la palabra que quieres encontrar: "))
  
  def busquedadicotomia(self, n):
    self.mitad = int(((len(dicotomia().tabla_ord)-1)/2) - n)
    if dicotomia().palabra == dicotomia().tabla_ord[self.mitad]:
      print("La palabra se encuentra en la posición " + str((self.mitad)+1))
    elif dicotomia().palabra < dicotomia().tabla_ord[self.mitad] and dicotomia().palabra > dicotomia().tabla_ord[(self.mitad)-1]:
      print("La palabra introducida no se encuentra en la lista de palabras.")
    else:
      if dicotomia().palabra < dicotomia().tabla_ord[self.mitad]:
        dicotomia().busquedadicotomia(n+1)
      else:
        dicotomia().busquedadicotomia(n-1)

  def __init__(self):
    dicotomia().busquedadicotomia(0)