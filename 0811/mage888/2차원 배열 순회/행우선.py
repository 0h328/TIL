import sys
sys.stdin = open("input.txt")

N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]

for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end=' ')