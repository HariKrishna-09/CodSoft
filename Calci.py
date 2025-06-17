a=int(input("Enter Digit 1: "))
b=int(input("Enter Digit 2: "))
op=input("Enter the operater: ")

match op:
   case '+':
      print("The Result is: ")
      print(a+b)
   case '-':
      print("The Result is: ")
      print(a-b)

   case '*':
      print("The Result is: ")
      print(a*b)

   case '/':
      if b!=0:
         print("The Result is: ")
         print(a/b)
      else:
         print("Error! Division by zero")

   case '%':
      if b!=0:
         print("The Result is: ")
         print(a%b)
      else:
         print("Error! Division by zero")

   case _:
      print("invalid operator")
