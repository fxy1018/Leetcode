'''
Created on Mar 3, 2017

@author: fanxueyi
'''

#two slow, recursive
#uses Θ(n) stack space and Θ(ϕn), arithmetic operations, where ϕ=5√+12 (the golden ratio), which grows exponentially. 
def fibonacci(n):
    if n == 0:
        return(0)
    if n == 1:
        return(1)
    
    return(fibonacci(n-1) + fibonacci(n-2))

#This algorithm takes Θ(1) space and Θ(n) operations.
def fibonacci2(n):
    if n == 0:
        return(0)
    if n == 1:
        return(1)
    fib1 = 0
    fib2 = 1
    for i in range(2, n+1):
        temp = fib2
        fib2 = fib2 + fib1
        fib1= temp     
    return(fib2)

#Matrix exponentiation (fast)
#https://www.nayuki.io/page/fast-fibonacci-algorithms
#This algorithm takes Θ(1) space and Θ(logn) operations.

def fibonacci3(n):
    if n < 0:
        raise ValueError("Negative arguments not implemented")
    return _fib(n)[0]


# (Private) Returns the tuple (F(n), F(n+1)).
def _fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = _fib(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)

print(fibonacci2(100))
