import sys

sys.stdin = open('input.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def delta_search(target):   # 같은 숫자 여러 개면 x, y 받아서 해야함
    for i in range(N):
        if target in arr[i]:
            y = i
            for j in range(N):
                if arr[i][j] == target:
                    x = j
                    break
            break

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        nxt_x = x + dx[i]
        nxt_y = y + dy[i]
        print(arr[nxt_y][nxt_x])

delta_search(5)

