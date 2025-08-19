#reverse a number

# n=int(input())
# rev=0
# while n:
#     rev= rev * 10 + n % 10 
#     n//=10
# print("Reversed :",rev )    



n=int(input())
rev=0
while n:
    rev=rev*10 + n % 10
    n//=10
print("Reversed :",rev)    