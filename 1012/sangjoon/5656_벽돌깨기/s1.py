# 문제 푼 시간
from collections import deque
from itertools import product
from copy import deepcopy


class Block:
    """
    블록에 대한 객체를 생성합니다.

    Attribultes:
        block: 벽돌을 담아놓는 블록

    Methods:
        build_blocks: 블록내 벽돌을 추가하거나 생성합니다.
        break_block: idx 위치의 벽돌을 부수고 그 값을 반환합니다.
        get_block_len: 블록내 벽돌을 개수를 반환합니다.
    """

    def __init__(self):
        self.block = deque([])

    def build_blocks(self, n: int):
        """
        블록을 위로 쌓습니다.
        """
        self.block.appendleft(n)

    def break_block(self, idx: int):
        """
        블록에 대한 idx를 받아 해당 위치의 블록의 값을 반환하고 삭제합니다.
        Returns:
            삭제된 벽돌의 값을 반환합니다.
        """
        e = self.block[idx]
        del self.block[idx]
        return e

    def get_block_len(self):
        """
        블록의 남은 벽돌의 개수를 반환합니다.
        Returns:
            블록의 남은 벽돌의 개수를 반환합니다.
        """
        return len(self.block)


# 깨야하는 블록의 리스트를 생성하는 dfs 함수
def dfs(x, idx):
    e = blocks[x].block[idx]
    tmp[0] += 1  # 부순 블록의 개수에 추가합니다.

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

    # 블록 객체 입력
    for _ in range(H):
        blks = list(map(int, input().split()))
        for i, n in enumerate(blks):
            if n:
                total += 1
                B[i].build_blocks(n)

    dp = dict()
    ans = [total]
    breaker = False

    # 부셔야할 벽돌에 대한 중복순열을 순회합니다.
    for moves in product([i for i in range(W)], repeat=N):
        blocks = deepcopy(B)
        tmp = [0]

        for i in range(N):
            if moves[:i] in dp:
                blocks = dp[moves[:i]]
                continue

            start = moves[i]
            l = blocks[start].get_block_len() - 1  # 시작지점을 탐색

            # 해당 위치에 블록이 있을 경우에만 dfs 탐색
            if l < 0:
                break

            breaks = [(start, l)]
            dfs(start, l)
            # 높은 위치부터 삭제해야하므로 높은 idx 순 정렬
            breaks.sort(key=lambda x: -x[1])
            for x, idx in breaks:
                blocks[x].break_block(idx)

            # 남은 벽돌의 최솟값 비교
            ans[0] = min(ans[0], total - tmp[0])

            # 남은 벽돌이 없을 경우, 탐색 종료
            if not ans[0]:
                breaker = True

            dp[moves[:i+1]] = deepcopy(blocks)

        if breaker:
            break

    print(dp)
    print(f"#{test_case} {ans[0]}")
