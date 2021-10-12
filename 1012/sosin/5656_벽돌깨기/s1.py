import sys
sys.stdin = open('input.txt')

from collections import deque

dr = [0,0,-1,1]
dc = [1,-1,0,0]

def shoot_ball(n, cblock):
    global result
    if n > N:
        result = min(result, sum_block(cblock))# 남은 블록 합계
        return

    for i in range(W):
        shoot_ball(n+1, remove_block(cblock, i))

import copy
def remove_block(blocks, pos):
    new_blocks = copy.deepcopy(blocks)
    for i, row in enumerate(new_blocks):
        if row[pos] != 0:
            break

    q = deque([(i, pos)])
    while q:
        r, c = q.popleft()
        temp = new_blocks[r][c]
        new_blocks[r][c] = 0
        for k in range(4):
            # 사방향 + 해당 블록의 숫자만큼 퍼져나감
            for nb in range(1, temp):
                nr = r+dr[k] * nb
                nc = c+dc[k] * nb
                if 0<=nr<H and 0<=nc<W and new_blocks[nr][nc]:
                    q.append((nr, nc))

    # 위에있는 블록 내려오기
    col_idx = [0]*W
    
    for row in new_blocks:
        for i, r in enumerate(row):
            if r == 0:
                cols[col_idx[i]]=r
                col_idx[i]+=1
    print(*cols, sep='\n')
    return cols

def sum_block(blocks):
    return sum([W - b.count(0) for b in blocks])

for T in range(int(input())):
    result = 1e9
    N, W, H = map(int, input().split())
    # 위에서만 떨어뜨릴 수 있음
    blocks = [list(map(int, input().split())) for _ in range(H)]
    shoot_ball(0, blocks)
    
    print('#{} {}'.format((T+1), result))

#1 12
#2 27
#3 4
#4 8
#5 0
