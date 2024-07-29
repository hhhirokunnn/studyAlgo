# https://leetcode.com/problems/powx-n/solution/

# RecursionError: maximum recursion depth exeeded in comparison.
# SEE: https://docs.python.org/3/library/sys.html#sys.setrecursionlimit
# it says default is 1000.
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1
        
        def _pow(num, exp):
            if exp == 0:
                return 1
            return num * _pow(num, exp - 1)
        
        if n >= 0:
            return _pow(x, n)
        
        return 1 / _pow(x, -n)
# O(n O(n

# https://www.geeksforgeeks.org/binary-exponentiation-for-competitive-programming/
# x^n = x*(x^2)^((n-1)/2) if n is odd
# x^n = (x^2)^(n/2)       if n is even
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def _pow(x, n):
            if n == 0:
                return 1
            if n % 2:
                return x * _pow(x * x, (n - 1) / 2)
            
            return _pow(x * x, n / 2)
        
        if n < 0:
            return 1 / _pow(x, -n)
            
        return _pow(x, n)
# O(logn, O(logn

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n < 0:
            n = -n
            x = 1.0 / x
        
        result = 1
        while n:
            if n % 2:
                result *= x
                n -= 1
            x *= x
            n //= 2
        return result
# O(logn, O(1
