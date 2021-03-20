import math

def fib(n):
    root = math.sqrt(5)
    ratio = (1 + root) / 2
    return int(ratio ** n / root + 0.5)

print (fib(int(input('Which Fibonacci number would you like?'))))
