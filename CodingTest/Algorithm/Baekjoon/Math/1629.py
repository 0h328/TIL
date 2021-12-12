import sys
sys.stdin = open('input.txt')

A, B, C = map(int, sys.stdin.readline().split())

def exp(A, B):
    if B == 1:
        return A % C
    else:
        res = exp(A, B//2)
        if B % 2 == 0:
            return res ** 2 % C
        else:
            return res ** 2 * A % C

print(exp(A, B))