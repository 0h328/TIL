import sys
sys.stdin = open('input.txt')

L = list(map(int, input().split()))

N = len(L)

for i in range(1<<N):
    for j in range(N+1):
        if i & (1<<j):
            print(L[j], end= ' ')
    print()
