import sys
sys.stdin = open('input.txt')

from collections import deque
import copy

dr = [0,0,-1,1]
dc = [1,-1,0,0]

def shoot_ball(n, cblock):
    global result
    if n >= N:
        result = min(result, sum_block(cblock)) # 남은 블록 합계
        return

    for i in range(W):
        shoot_ball(n+1, remove_block(cblock, i))


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
                    if (nr, nc) not in q:
                        q.append((nr, nc))

    return buck_down(new_blocks)

def buck_down(new_blocks):
    # 위에있는 블록 내리기
    update_block = [[0]*W for _ in range(H)]
    for w in range(W):
        temp = []
        for h in range(H):
            if new_blocks[h][w]:
                temp.append(new_blocks[h][w])
        for i in range(len(temp)):
            update_block[H-len(temp)+i][w] = temp[i]

    return update_block

def sum_block(blocks):
    return sum([W - b.count(0) for b in blocks])

for T in range(int(input())):
    result = 1e9
    N, W, H = map(int, input().split())

    blocks = [list(map(int, input().split())) for _ in range(H)]
    shoot_ball(0, blocks)
    
    print('#{} {}'.format((T+1), result))

#1 12
#2 27
#3 4
#4 8
#5 0
