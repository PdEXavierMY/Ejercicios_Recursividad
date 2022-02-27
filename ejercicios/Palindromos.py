class Palindromo():
  def espalindromo(self):
    self.frase = str(input("Introduce la palabra/frase a analizar: ")).lower()
    i, j = "áéíóúñ" , "aeioun"
    self.tilde = str.maketrans(i, j)
    self.frase = self.frase.translate(self.tilde)
    self.frase_sep = self.frase.split()
    
    print("".join(self.frase_sep)[::-1])
    print("".join(self.frase_sep))
    
    if ("".join(self.frase_sep)[::-1]) == ("".join(self.frase_sep)):
      print("Es un palíndromo.")
    else:
      print("No es un palíndromo.")
  
  def iniciar(self):
    Palindromo().espalindromo()