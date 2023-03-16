import art

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1/n2


operations = {
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}

def calculator():
  print(art.logo)

  n1 = float(input('What is the first number? '))

  Continue = True
  
  while Continue is True:
    for symbol in operations:
      print(symbol)
    operation = input('Which operation would you like to use? ')
    n2 = float(input('What is the second number? '))
    calculation = operations[operation]
    answer = calculation(n1,n2)
    print(f"{n1} {operation} {n2} = {answer}")
    calc = input(f'If you would like to use {answer} in another calculation type "yes", type "no" if you would like to start a new calculation? ').lower()
    if calc == 'yes':
      n1 = answer
    elif calc == 'no':
      Continue = False
      calculator()

calculator()