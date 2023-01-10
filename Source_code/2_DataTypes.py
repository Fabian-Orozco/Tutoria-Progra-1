import random

def main():
  """Para utilizar comillas dobles dentro de un string, se utiliza caracter de escape \ o comillas simples de apertura y cierre"""
  Frase = 'Esta es una frase de Gandhi "asdjkasd"   '
  Frase_2 = "Esta es una frase de Gandhi \"asdjkasd\"   "
  Frase_3 = 6
  print(Frase_2)
  print(Frase)
  print(type(Frase_3))

  """ 
  Bool (George Boole)
      T=1=V     | F=0=F
      Verdadero | Falso
  """
  esVerde = False
  esAzul = True
  miDatoNone = None
  print(type(miDatoNone))

  """ En C++: 
    Declarar un objeto: Carro car = new Carro(4)
    public Carro(tipo numeroDePuertas) {
      this.numeroDePuertas = numeroDePuertas
    } 
  """

  """ Casting (cambiar el tipo de dato) """
  convertido = str(2)
  print(type(convertido))

  y = 1.2e4
  print(int(y))

  """ Random number [start, stop["""
  print(random.randrange(1, 10))

  stringGrande = '''Lorem ipsum dolor sit amet,
  consectetur adipiscing elit,
  sed do eiusmod tempor incididunt
  ut labore et dolore magna aliqua.'''
  print(stringGrande)

  """String son un array por debajo. Cada posición es un caracter. Inicia siempre en 0"""
  saludo = "Hello, World!"
  print(saludo[1])

  """Recorriendo cada letra"""
  for letra in "banana":
    print(letra)

  """Obtener la longitud(largo) de cada string"""
  frase = "hola me llamo Fabian"
  print(len(frase))

  """Chequear existencia de una parte de texto"""
  txt = "The best things in life are free!"
  print("free" in txt)

  """
    El not invierte/niega el True o False.
    si x es True entonces (not x) es False
    si x es False entonces (not x) es True
  """
  txt = "The best things in life are free!"
  print("expensive" not in txt)

  saludo_2 = "Hello, World!"
  print(saludo_2[2:])

  """Con un "-" recorre de forma inversa (de derecha a izquierda)"""
  print(saludo_2[-1])
  print(saludo_2[-5:-2])

  a = "Hello, World!"
  print(a.replace("H", "J"))
  """ Si quiere que se asigne el nuevo valor, tiene que indicarlo.
  Las funciones crean copias de los strings originales, no trabajan sobre ellos sobreescribiendolos"""
  a = a.replace("H", "J")
  print(a)

  a = "Hello, World!, Again"
  print(a.split(","))

  """String format: reemplaza los corchetes con el valor pasado por parámetro al format"""
  age = 36
  txt = "My name is John, and I am {}"
  print(txt.format(age))

  quantity = 3
  itemno = 567
  price = 49.95
  myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
  print(myorder.format(quantity, itemno, price))

if __name__ == '__main__':
  main()

