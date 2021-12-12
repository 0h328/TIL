import sys
sys.stdin = open('input.txt')

n, m = map(int, sys.stdin.readline().split())
def fact(n):
    if n <= 1:
        return 1

    return n * fact(n-1)

print(fact(n)//(fact(m)*fact(n-m)))