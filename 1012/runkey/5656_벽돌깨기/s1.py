"""
① 구슬은 좌, 우로만 움직일 수 있어서 항상 맨 위에 있는 벽돌만 깨트릴 수 있다.
② 벽돌은 숫자 1 ~ 9 로 표현되며,
   구슬이 명중한 벽돌은 상하좌우로 ( 벽돌에 적힌 숫자 - 1 ) 칸 만큼 같이 제거된다.
"""

import sys
sys.stdin = open('input.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, n):
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]

        # if 0 <= nr < H and 0 <= nc < W:


tc = int(input())

for t in range(1, 2):
    result = 0
    N, W, H = map(int, input().split())
    N_list = [list(map(int, input().split())) for _ in range(H)]
    print(N_list)
    col_sum = []
    row_sum = []
    while N != 0:
        print(N)
        for i in range(H):
            row_sum.append(sum(N_list[i]))
            temp = 0
            for j in range(W):
                temp += N_list[j][i]
            col_sum.append(temp)
        N -= 1
        max_row = max(row_sum)
        max_row_index = row_sum.index(max_row)
        max_row_col_index = N_list[max_row_index].index(max(N_list[max_row_index]))

        max_col = max(col_sum)
        max_col_index = col_sum.index(max_col)
        temp_col = 0
        temp_index = 0
        for r in range(H):
            if temp_col < N_list[r][max_col_index]:
                temp_col = N_list[r][max_col_index]
                temp_index = r
        max_col_row_index = temp_index
    print("#{} {}".format(t, result))