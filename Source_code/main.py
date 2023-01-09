# Variable global
miPerro = "Jack"

def myfunc():
  print("Mi perro se llama " + miPerro)

myfunc()

# -------------------------------
""" El valor de la variable local funciona dentro del scope de la función, no sobreescribe la global"""
def myfunc():
  miPerro = "Fluffy"
  print("Mi perro se llama " + miPerro)

myfunc()
print("Mi perro se llama " + miPerro)
# -------------------------------

""" El valor de la variable se re-declara con el keyword "global" que sobreescribe la variable global"""
def myfunc():
  global miPerro
  miPerro = "Fluffy"
  print("Mi perro se llama " + miPerro)

myfunc()
print("Mi perro se llama " + miPerro)
# -------------------------------

# Es una constante
MAX_LENGTH = 8

def main():
  miNumero = 5
  nombre = "Fabian"
  Nombre = "Maikol"

  """ Concatenación: se hace con +
      Sirve para unir cadenas (Strings)
      Si se quiere unir con integers, se utiliza la ,
  """
  # print("Este es mi numero:" , miNumero)

  # Asignación en una sola línea
  x, y = "Granja", "Edificio"
  # print("x es igual a: " + x + " y es igual a: " + y)
  
  x = y = "Pato"
  # print("x es igual a: " + x + " y es igual a: " + y)

  edad = numeroZapatos = 0

  """Declarar varias variables desde un arreglo"""
  fruits = ["apple", "banana", "cherry"]
  x, y, z = fruits
  # print(x + y + z)


"""Esta es una función y siempre se declara en infinitivo"""
def sumar(numero1, numero2):
  # Operadores aritmeticos: + , - , / , *, ** , % , //
  return numero1 + numero2

def restar(numero1, numero2):
  return numero1 - numero2

if __name__ == '__main__':
  main()
  resultado1 = sumar(10, 5)
  # print("El resultado de la suma es:" , resultado1)
  # print("el resultado de la resta es:", restar(resultado1, 4))