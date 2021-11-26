from collections import deque
import sys

sys.stdin = open('input.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
INF = 10000000

def bfs(r, c):
    q = deque()
    q.append((r, c))
    dist[r][c] = 0

    while q:
        cur_r, cur_c = q.popleft()

        for d in range(4):
            nxt_r = cur_r + dr[d]
            nxt_c = cur_c + dc[d]

            if 0 <= nxt_r < N and 0 <= nxt_c < N:
                diff = data[nxt_r][nxt_c] - data[cur_r][cur_c] if data[nxt_r][nxt_c] > data[cur_r][cur_c] else 0
                if dist[nxt_r][nxt_c] > dist[cur_r][cur_c] + 1 + diff:
                    dist[nxt_r][nxt_c] = dist[cur_r][cur_c] + 1 + diff
                    q.append((nxt_r, nxt_c))

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    data = [list(map(int, input().split())) for _ in range(N)]
    dist = [[INF] * N for _ in range(N)]

    bfs(0, 0)
    ans = dist[N-1][N-1]

    print('#{} {}'.format(tc, ans))