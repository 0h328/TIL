from collections import deque
import sys

sys.stdin = open("input.txt")

T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    q = deque()
    q.append((r, c))
    start_num = data[r][c]
    visited[r][c] = start_num
    cnt = 1

    while q:
        cur_r, cur_c = q.popleft()
        for d in range(4):
            nxt_r = cur_r + dr[d]
            nxt_c = cur_c + dc[d]

            if 0 <= nxt_r < N and 0 <= nxt_c < N:
                if not visited[nxt_r][nxt_c] or visited[nxt_r][nxt_c] > start_num:
                    if data[cur_r][cur_c] + 1 == data[nxt_r][nxt_c]:
                        q.append((nxt_r, nxt_c))
                        visited[nxt_r][nxt_c] = start_num
                        cnt += 1
                        break

    if cnt > ans[1]:
        ans[0] = start_num
        ans[1] = cnt
    elif cnt == ans[1]:
        if ans[0] > start_num:
            ans[0] = start_num


for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]

    ans = [0, 0]  # 처음 방 번호, 이동 방 개수

    for row in range(N):
        for col in range(N):
            if not visited[row][col]:
                bfs(row, col)

    print("#{}".format(tc), end=" ")
    print(*ans)
