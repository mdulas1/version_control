print("calculator")
num1 = float(input("enter firstnum1\n>"))
num2 = float(input("enter firstnum2\n>"))
operator = input("select oprator\n>>")
if operator == "+":
  print(num1 + num2)

elif operator == "-":
  print(num1 - num2)

elif operator == "*":
  print(num1 * num2)

elif operator == "/":
  if num2 == 0:
    print("complexInfinity")

  else:
    print(num1 / num2)

else:
  print("invalid input")
