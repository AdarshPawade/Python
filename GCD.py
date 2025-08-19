#GCD
a=int(input("Enter a: "))
b=int(input("Enter b: "))
small=min(a,b)
for i in range(1,small+1):
    if(a%i==0 and b%i==0):
        gcd=i
print("GCD  is",gcd)
   