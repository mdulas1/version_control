print("calculator using oop")
class Calculator:
  def __init__(self):
    print("basic calculator")

  def add(self,a,b):
    return a + b
  
  def mul(self,a,b):
    return a * b
  
  def sub(self,a,b):
    return a - b
  
  def div(self,a,b):
    if b == 0:
      return "complexInfinity"
    return a / b
cal = Calculator()
u = cal.div(1500,5)
print(u)