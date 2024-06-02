#This code contains calculator logo imported from calculator art module.
#visit : https://replit.com/@devmoh04/calculator-final#art.py for the logo module.

from replit import clear
from art import logo


def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  tocontinue = True
 
  while tocontinue:
    user_operation = input("Choose the operation to perform: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[user_operation]
    result = calculation_function(num1, num2)
    print(f"{num1} {user_operation} {num2} = {result}")

    if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") == 'y':
      num1 = result
    else:
      tocontinue = False
      clear()
      calculator()

calculator()
