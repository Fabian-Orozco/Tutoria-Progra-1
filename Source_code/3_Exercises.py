def sumar(a, b):
  return a + b

def read():
  a, b = input().split(' ')
  return a, b

cases = int(input())
for line in range(cases):
  lista = read()
  primerNumero = int(lista[0])
  segundoNumero = int(lista[1])

  print(sumar(primerNumero, segundoNumero))

'''
Problem Statement
The task is very simple: given two integers A and B, write a program to add these two numbers and output it.

Input Format
The first line contains an integer T, the total number of test cases. Then follow T lines, each line contains two Integers A and B.

Constraints
1 ≤ T ≤ 1000
0 ≤ A,B ≤ 10000
'''