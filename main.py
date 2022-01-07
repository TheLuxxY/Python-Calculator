print("Operators")
print("For Sum = +")
print("For Sub = -")
print("For Multiplication = *")
print("For Division = /")

def mul(a, b):
  result = a * b
  print(result)
  
 


def div(a, b):
  result= a / b
  print(result)
  
  

def add(a, b):
  result= a + b
  print(result)
  
  
def min(a, b):
  result = a - b
  print(result)
  
  
a = int(input("Enter First Number:"))
b = int(input("Enter Second Number:"))
op = input("Enter Operator:")

if op=="+":
  add(a, b)
  
  
elif op=="-":
  min(a, b)
  
elif op=="*":
  mul(a, b)
  
elif op =="/":
  div(a, b)
  
else:
  print("Invalid Operator")
    