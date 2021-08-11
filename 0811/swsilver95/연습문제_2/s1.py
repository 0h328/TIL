import sys

sys.stdin = open('input.txt')

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]              # 상하좌우
dy = [0, 0, -1, 1]


for i in range(1, len(arr) - 1):
    for j in range(1, len(arr[0]) - 1):
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            print(arr[nx][ny])

