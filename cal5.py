# calculator functions
print("calculator using function")

def add(a,b):
  return a + b

def mul(a,b):
  return a * b

def sub(a,b):
  return a - b

def div(a,b):
  if b == 0:
    return f"error"
  return a / b

addition = add(6,9)
multiplication = mul(6,2)
subtraction = sub(7,3)
division = div(1,9)
print(division)