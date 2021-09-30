import sys

sys.stdin = open("input.txt")
from collections import deque

T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


for tc in range(1, T + 1):
    N, M = map(int, input().split())

    visited = [[-1] * M for _ in range(N)]  # data에 넣으면서 하면 15개에서 시간 초과
    queue = deque()
    cnt = 0

    for row in range(N):
        temp = list(input())
        for col in range(M):
            if temp[col] == "W":
                visited[row][col] = 0
                queue.append((row, col))
                cnt += 1

    ans = 0

    while queue:
        cur_row, cur_col = queue.popleft()

        for i in range(4):
            nxt_row = cur_row + dr[i]
            nxt_col = cur_col + dc[i]

            if 0 <= nxt_row < N and 0 <= nxt_col < M:
                if visited[nxt_row][nxt_col] == -1:
                    visited[nxt_row][nxt_col] = visited[cur_row][cur_col] + 1
                    queue.append((nxt_row, nxt_col))
                    ans += visited[nxt_row][nxt_col]
                    cnt += 1

        if cnt == N * M:
            break

    print("#{} {}".format(tc, ans))
