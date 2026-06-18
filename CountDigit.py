#count digits in number 

n=int(input())
count=0
while n:
    count+=1
    n//=10
print("Digits :",count)
print("Modified file")