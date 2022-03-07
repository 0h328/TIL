import sys
sys.stdin = open('input.txt')

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

def lcm(x, y):
    return x*y // gcd(x, y)

A, B = map(int, sys.stdin.readline().split())
print(lcm(A, B))