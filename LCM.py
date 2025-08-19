a=int(input("Enter a: "))
b=int(input("Enter b: "))
res=max(a,b)
while(res<=a*b):
    if(res%a==0 and res%b==0):
        break
    res+=1
print(res)        