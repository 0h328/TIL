import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)

#1. 행 우선순회
for i in range(N):
    for j in range(M):
        print(arr[i][j], end=' ')
    print()

#2. 열 우선 순회
for i in range(M):
    for j in range(N):
        print(arr[j][i], end=' ')
    print()