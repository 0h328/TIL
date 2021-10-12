import sys
from collections import deque
sys.stdin = open('input.txt')

def arrange_brick(brick): #존재하는 값 정렬하는 함수
    arr_brick = [[0]*w for _ in range(h)]
    for j in range(w): #한개의 열을 보기 위해서
        temp = []
        for i in range(h):
            if brick[i][j]: # 값이 존재한다면
                temp.append(brick[i][j])
        for k in range(len(temp)):
            arr_brick[h-len(temp)+k][j] = temp[k] # 전체 행의 높이중에서 - 존재하는 값을 빼고 + 인덱스 처리
    return arr_brick


def solve(row, col, brick_num):
    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]
    que = deque()
    que.append((row, col, brick_num))
    while que:
        row, col, brick_num = que.popleft()
        brick[row][col] = 0
        for i in range(4):
            for num in range(1, brick_num):
                nr = row + dr[i]*num
                nc = col + dc[i]*num
                if 0 <= nr < h and 0 <= nc < w and not brick[nr][nc]:
                    if brick[nr][nc] != 1:
                        que.append((nr, nc, brick[nr][nc]))
                    brick[nr][nc] = 0

for tc in range(int(input())):
    n, w, h = list(map(int, input().split()))
    brick = [list(map(int, input().split())) for _ in range(h)]

    while n > 0:
        for i in range(h):
            for j in range(w):
                if brick[i][j] != 0:
                    solve(i, j, brick[i][j])
                    break
                break
            break
        arrange_brick(brick)
        n -= 1
    for b in brick:
        print(b, sep = '\n')