import sys
sys.stdin = open('input.txt')

def fibo(n):
    if n > 1000000:
        return None

    if n < 2:
        return n

    a, b = 0, 1

    for i in range(n - 1):
        a, b = b%1000000007, (a + b)%1000000007

    return b


print(fibo(int(input())))