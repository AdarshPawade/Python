class Solution:
    def isprime(self,n:int):
        for i in range(2,n):
            if n%i==0:
                return False
        return True  
        
        
        
    def printPrimeFactorization(self, n:int):
        #code here
        for i in range(2,n+1):
            if self.isprime(i):
                x=i
                while n%x==0:
                    print(i,end=" ")
                    x=x*i




                    