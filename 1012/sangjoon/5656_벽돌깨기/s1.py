# 문제 푼 시간
from collections import deque
from itertools import product
from copy import deepcopy

# 위로 쌓은 블록에 대한 객체 생성


class Block:
    def __init__(self):
        self.block = deque([])

    def build_blocks(self, n: int):
        self.block.appendleft(n)

    def break_block(self, idx: int):
        e = self.block[idx]
        del self.block[idx]
        return e

    def get_block_len(self):
        return len(self.block)

# 깨야하는 블록의 리스트를 생성하는 dfs 함수


def dfs(x, idx):
    e = blocks[x].block[idx]
    tmp[0] += 1

    dx = [0, 0, 1, -1]
    didx = [1, -1, 0, 0]

    for i in range(1, e):  # 이동가능 벽돌의 개수
        for j in range(4):  # 4개의 방향에 대한
            nx = x + dx[j]*i
            nidx = idx + didx[j]*i
            if 0 <= nx < W and 0 <= nidx < blocks[nx].get_block_len():
                if (nx, nidx) not in breaks:
                    breaks.append((nx, nidx))
                    dfs(nx, nidx)


test = int(input())

for test_case in range(1, test+1):
    N, W, H = map(int, input().split())
    B = [Block() for _ in range(W)]
    total = 0
    for _ in range(H):  # 벽돌 생성
        blks = list(map(int, input().split()))
        for i, n in enumerate(blks):
            if n:  # 벽돌이 있을 경우에만
                total += 1
                B[i].build_blocks(n)

    ans = [total]
    breaker = False
    # 부수는 벽돌에 대한 방법
    for moves in product([i for i in range(W)], repeat=N):
        blocks = deepcopy(B)
        tmp = [0]
        for start in moves:
            l = blocks[start].get_block_len() - 1  # 시작지점 탐색
            if l >= 0:
                breaks = [(start, l)]
                dfs(start, l)
                # 높은 위치부터 삭제해야하므로 높은 idx 순 정렬
                breaks.sort(key=lambda x: -x[1])
                for x, idx in breaks:
                    blocks[x].break_block(idx)
                ans[0] = min(ans[0], total - tmp[0])
            if not ans[0]:
                breaker = True
        if breaker:
            break

    print(f"#{test_case} {ans[0]}")
