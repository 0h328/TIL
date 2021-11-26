import sys
import copy
sys.stdin = open('input.txt')

di = [0, -1, 0, 1] #우, 하, 좌, 상
dj = [1, 0, -1, 0]
def bomb(i, j, cnt):
    if cnt == N:
        return
    stack = []
    stack.append((i, j, blocks[i][j]))


    for k in range(4):
        for idx in range(blocks[i][j]-1):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                temp_blocks[ni][nj] -= 10
                i = ni
                j = nj
    for i in range(H):
        for j in range(W):
            temp_blocks[i][j] += blocks[i][j]
    stack.pop(0)


T = int(input())

for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    blocks = [list(map(int, input().split())) for _ in range(H)]

    cnt = 0
    temp_blocks = [[-10 for _ in range(W)] for _ in range(H)]
    temp = copy.deepcopy(blocks)
    print(temp)
    print(temp_blocks)
    # for i in range(H):
    #     for j in range(W):
    #         if blocks[i][j] != 0:
    #             bomb()