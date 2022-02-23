import sys
sys.stdin = open('input.txt')

t = int(input())
for _ in range(t):
    n = int(input())
    fib = [1, 1, 2, 4]

    for i in range(4, n+1):
        fib.append(fib[i-4] + fib[i-3] + fib[i-2] + fib[i-1])

    print(fib[n])

