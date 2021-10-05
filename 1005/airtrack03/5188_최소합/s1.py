import sys
from collections import deque
sys.stdin = open('input.txt')

dr = [1, 0]
dc = [0, 1]

def bfs(start):
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] += data[start[0]][start[1]]

    while q:
        cur_row, cur_col = q.popleft()

        for d in range(2):
            nxt_row = cur_row + dr[d]
            nxt_col = cur_col + dc[d]

            if nxt_row < N and nxt_col < N:
                if not visited[nxt_row][nxt_col]:
                    visited[nxt_row][nxt_col] = visited[cur_row][cur_col] + data[nxt_row][nxt_col]
                    q.append((nxt_row, nxt_col))
                else:
                    if visited[nxt_row][nxt_col] > visited[cur_row][cur_col] + data[nxt_row][nxt_col]:
                        visited[nxt_row][nxt_col] = visited[cur_row][cur_col] + data[nxt_row][nxt_col]



T = int(input())

for tc in range(1, T+1):
    N = int(input())

    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    bfs((0, 0))

    print('#{} {}'.format(tc, visited[N-1][N-1]))