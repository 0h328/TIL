import sys
sys.stdin = open('input.txt')

A, B = [], []

N, M = map(int, input().split())

for r in range(N):
    r = list(map(int, input().split()))
    A.append(r)

for r in range(N):
    r = list(map(int, input().split()))
    B.append(r)

for r in range(N):
    for c in range(M):
        print(A[r][c] + B[r][c], end=' ')
    print()