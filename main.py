# calculator
import clear

# inputs
n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
# operator choice
choice = input("Select an operator ('+, -, *, /'): ")

# adding
def add(n1, n2):
  return n1 + n2

# subtracting
def subtract(n1, n2):
  return n1 - n2

# multiplying
def multiply(n1, n2):
  return n1 **  n2

# dividing
def divide(n1, n2):
  return n1 / n2

# logic depending on what operator is chosen
if choice == '+':
  answer = add(n1, n2)
elif choice == '-':
  answer = subtract(n1, n2)
elif choice == '*':
  answer = multiply(n1, n2)
elif choice == '/':
  answer = divide(n1, n2)

# asking the user if they want to continue with the number they just returned
continue_question = input("Do you want to continue with the number returned? Answer 'Yes' or 'No': ")
if continue_question.lower() == "yes":
  # asking for second round of inputs for second calculation
  n3 = int(input("Enter another number to work with the number you just calculated: "))
  second_operator = input("Select an operator ('+, -, *, /'): ")
  
  def add(answer, n3):
    return answer + n3

# subtracting
  def subtract(answer, n3):
    return answer - n3

# multiplying
  def multiply(answer, n2):
    return n1 **  n3

# dividing
  def divide(answer, n3):
    return n1 / n3

  if choice == '+':
    print(add(answer, n3))
  elif choice == '-':
    print(subtract(answer, n3))
  elif choice == '*':
    print(multiply(answer, n3))
  elif choice == '/':
    print(divide(answer, n3))
else:
  print('clear')