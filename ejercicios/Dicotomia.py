tabla = ["cantar", "estupefacto", "incrédulo", "casa", "perro", "dormir", "leer", "planta", "libro", "soñar", "Word", "carrera", "disfrutar", "Qué?", "odio", "vida", "juega", "suspender", "aprobado", "decepción", "descanso", "alegría", "No", "manchar", "actitud", "Pedro", "hoy", "baúl", "bailar", "seis", "más", "palabras", "casi", "llegar", "negro"]
tabla_ord = sorted(tabla)
print(tabla_ord)
palabra = str(input("Introduce la palabra que quieres encontrar: "))

def busquedadicotomia(n):
  mitad = int(((len(tabla_ord)-1)/2) - n)
  if palabra == tabla_ord[mitad]:
    print("La palabra se encuentra en la posición " + str(mitad))
  elif palabra < tabla_ord[mitad]:
    busquedadicotomia(n+1)
  else:
    busquedadicotomia(n-1)
busquedadicotomia(0)