import sys

sys.setrecursionlimit(15000)

fibonaccis = {}

print('hello')

def fibbonaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        try:
            return fibonaccis[n]
        except:
            fibonaccis[n] = fibbonaci(n - 1) + fibbonaci(n -2)
            return fibonaccis[n]

print(fibbonaci(int(input('Which Fibonacci number do you want: '))))
