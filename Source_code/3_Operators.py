def main():

  """
  Comparar valores.
  La condición retorna True o False
  """
  a = 200
  b = 33

  if b > a:
    print("b is greater than a")
  else:
    print("b is not greater than a")

  """Casting a boolean. Todo lo que esté vacío va a ser false."""
  print(bool("Hello"))
  print(bool(15))
  print(bool(""))
  print(bool(0))
  print(bool(None))

  num = 200
  print(isinstance(num, int))

  """Operadores aritméticos"""
  """Operadores asignación"""
  """es lo mismo decir 
    x = x + 3
    x += 3
  """
  x = 5
  print ("x es:", x)
  x = x + 3
  print ("x = x + 3:", x)
  x += 3
  print ("x += 3:", x)

  """Operadores comparación ==, !=, >, <, >=, <="""
  """Operadores lógicos 
    En otros lenguajes: &&, ||, ! 
    En python: and (se deben cumplir ambas condiciones para que retorne True), or (se cumple al menos una condición para que retorne True), not (invierte el resultado final)
  """

  print("\nEjercicio con NOT")
  print("not(x < 5 and x < 10)")
  print("x:", x)
  print("x < 5:", x < 5)
  print("x < 10:", x < 10)
  print("x < 5 and x < 10:", x < 5 and x < 10)
  print("not(x < 5 and x < 10):", not(x < 5 and x < 10))

  """Operadores de identidad: para verificar si es el mismo objeto"""
  print("\nProbando el operador de identidad")
  x = ["apple", "banana"]
  y = ["apple", "banana"]
  z = x

  print(x is z)
  # returns True because z is the same object as x

  print(x is y)
  # returns False because x is not the same object as y, even if they have the same content

  print(x == y)
  # to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

  """Operador de membresía"""
  x = ["apple", "banana"]
  print("banana" in x)
  # returns True because a sequence with the value "banana" is in the list

  """Operadores Bitwise: &, I, ^, ~, <<, >>"""

  numero = input("Digite su número: ")
  print("numero ingresado: " + numero)

def mayorQue(num1, num2):
  if num1 > num2:
    return True
  else:
    return False

if __name__ == '__main__':
  main()
  print("Probando la función mayor que:", mayorQue(5, 4))
  
