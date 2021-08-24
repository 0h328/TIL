import sys
sys.stdin = open('input.txt')

A = list(map(int,input().split()))
N = len(A)

bit = [0] * N

for i in range(1 << N):
    for j in range(N):
        if i & (1 << j):
            print(A[j], end=' ')
    print()
print()




