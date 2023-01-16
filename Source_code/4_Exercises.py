# 1 ################################

cases = int(input())

for case in range(cases):
  numbers = input().split(' ')
  limiteMenor = int (numbers[0])
  limiteMayor = int (numbers[1])
  edad = int (numbers[2])

  if limiteMenor <= edad and limiteMayor > edad:
    print('YES')
  else:
    print('NO')

'''
Problem Statement
Problem
Chef wants to appear in a competitive exam. To take the exam, there are following requirements:

Minimum age limit is 

X (i.e. Age should be greater than or equal to 

X).
Age should be strictly less than 

Y.
Chef's current Age is 

A. Find whether he is currently eligible to take the exam or not.

Input Format
First line will contain 

T, number of test cases. Then the test cases follow.
Each test case consists of a single line of input, containing three integers ,X,Y, and 

A as mentioned in the statement.
Output Format
For each test case, output YES if Chef is eligible to give the exam, NO otherwise.

You may print each character of the string in uppercase or lowercase (for example, the strings YES, yEs, yes, and yeS will all be treated as identical).

Input:
5
21 34 30
25 31 31
22 29 25
20 40 15
28 29 28
'''

# 2 ################################
minimum = 2000
cases = int(input())

for case in range(cases):
    drinkToday = int(input())
    if drinkToday >= minimum:
        print("yes")
    else:
        print("no")
'''
Problem
Recently, Chef visited his doctor. The doctor advised Chef to drink at least 2000 ml of water each day.

Chef drank X ml of water today. Determine if Chef followed the doctor's advice or not.

Input Format
The first line contains a single integer T — the number of test cases. Then the test cases follow.
The first and only line of each test case contains one integer 
X — the amount of water Chef drank today.
Output Format
For each test case, output YES if Chef followed the doctor's advice of drinking at least 
2000
2000 ml of water. Otherwise, output NO.

You may print each character of the string in uppercase or lowercase (for example, the strings YES, yEs, yes, and yeS will all be treated as identical).
'''

# 3 ################################

cases = int(input())

for case in range(cases):
    data = input().split(' ')
    weeks = int(data[0])
    days = int(data[1])
    print (weeks * days)

'''
Problem
According to a recent survey, Biryani is the most ordered food. Chef wants to learn how to make world-class Biryani from a MasterChef. Chef will be required to attend the MasterChef's classes for X weeks, and the cost of classes per week is 

Y coins. What is the total amount of money that Chef will have to pay?

Input Format
The first line of input will contain an integer T — the number of test cases. The description of T test cases follows.
The first and only line of each test case contains two space-separated integers X and Y, as described in the problem statement.
Output Format
For each test case, output on a new line the total amount of money that Chef will have to pay.
'''