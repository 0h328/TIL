import sys
sys.stdin = open('input.txt')

def fibo(n):

    if n > 20:
        return None

    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(int(input())))