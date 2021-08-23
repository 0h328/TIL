import sys
sys.stdin = open("input.txt")

N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        print(A[i][j+(N-1-2*j)*(i % 2)], end=' ')
print()

for i in range(N):
    if i % 2 == 0:
        for j in range(N):
            print(A[i][j], end=' ')
    else:
        for j in range(N-1,-1,-1):
            print(A[i][j], end=' ')

