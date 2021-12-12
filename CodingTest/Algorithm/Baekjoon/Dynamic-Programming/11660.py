import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().strip().split())
arr = [[0] * (N+1)] + [[0] + list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

for i in range(1, N+1):
    for j in range(1, N):
        arr[i][j+1] += arr[i][j]

for j in range(1, N+1):
    for i in range(1, N):
        arr[i+1][j] += arr[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(arr[x2][y2] - arr[x1-1][y2] - arr[x2][y1-1] + arr[x1-1][y1-1])

