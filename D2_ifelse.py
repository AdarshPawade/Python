num1=input("enter num 1 :")
num2=input("enter num 2: ")
num3=input("enter num 3: ")

if num1 > num2 > num3:
    if num1 > num3 :
       print(f"{num1} is greater")
elif num2 > num1 > num3:
    if num2 > num3:
      print(f"{num2}is greater")    
else:
   print(f"{num3} is greater")      