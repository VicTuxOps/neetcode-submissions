class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n
        
        def pow(x,n):
            if n == 0:
                return 1
            if n == 1:
                return x
            
            half = pow(x,n//2)
            
            if n%2 == 0:
                return half * half
            else:
                return half * half * x
        
        return pow(x,n)