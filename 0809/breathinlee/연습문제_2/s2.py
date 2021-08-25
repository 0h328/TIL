import sys
sys.stdin = open("input.txt")

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 행 우선 순회
for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()

# 열 우선 순회
for j in range(m):
    for i in range(n):
        print(arr[i][j], end=' ')
    print()