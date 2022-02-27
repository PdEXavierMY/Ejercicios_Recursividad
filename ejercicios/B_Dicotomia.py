class dicotomia():
  def busquedadicotomia(self, n, tabla, palabra):
    self.mitad = int(((len(tabla)-1)/2) - n)
    if palabra == tabla[self.mitad]:
      print("La palabra se encuentra en la posición " + str((self.mitad)+1))
    elif palabra < tabla[self.mitad] and palabra > tabla[(self.mitad)-1]:
      print("La palabra introducida no se encuentra en la lista de palabras.")
    else:
      if palabra < tabla[self.mitad]:
        dicotomia().busquedadicotomia(n+1, tabla, palabra)
      else:
        dicotomia().busquedadicotomia(n-1, tabla, palabra)

  def iniciar(self):
    self.tabla = ["cantar", "estupefacto", "incrédulo", "casa", "perro", "dormir", "leer", "planta", "libro", "soñar", "Word", "carrera", "disfrutar", "Qué?", "odio", "vida", "juega", "suspender", "aprobado", "decepción", "descanso", "alegría", "No", "manchar", "actitud", "Pedro", "hoy", "baúl", "bailar", "seis", "más", "palabras", "casi", "llegar", "negro"]
    self.tabla_ord = sorted(self.tabla)
    print(self.tabla_ord)
    self.palabra = str(input("Introduce la palabra que quieres encontrar: "))
    dicotomia().busquedadicotomia(0, self.tabla_ord, self.palabra)