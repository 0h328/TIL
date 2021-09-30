from collections import deque

T = int(input())

paths = {
    1: {0: [1, 2, 5, 6], 1: [1, 2, 4, 7], 2: [1, 3, 4, 5], 3: [1, 3, 6, 7]},
    2: {0: [1, 2, 5, 6], 1: [1, 2, 4, 7], 2: [], 3: []},
    3: {0: [], 1: [], 2: [1, 3, 4, 5], 3: [1, 3, 6, 7]},
    4: {0: [1, 2, 5, 6], 1: [], 2: [], 3: [1, 3, 6, 7]},
    5: {0: [], 1: [1, 2, 4, 7], 2: [], 3: [1, 3, 6, 7]},
    6: {0: [], 1: [1, 2, 4, 7], 2: [1, 3, 4, 5], 3: []},
    7: {0: [1, 2, 5, 6], 1: [], 2: [1, 3, 4, 5], 3: []},
}

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = 1
    cnt = 1

    while queue:
        cur_row, cur_col = queue.popleft()

        for i in range(4):
            nxt_row = cur_row + dr[i]
            nxt_col = cur_col + dc[i]

            if 0 <= nxt_row < N and 0 <= nxt_col < M and not visited[nxt_row][nxt_col]:
                if (
                    data[nxt_row][nxt_col]
                    and data[nxt_row][nxt_col] in paths[data[cur_row][cur_col]][i]
                ):
                    visited[nxt_row][nxt_col] = visited[cur_row][cur_col] + 1
                    if visited[nxt_row][nxt_col] > L:
                        return cnt
                    cnt += 1
                    queue.append((nxt_row, nxt_col))

    return cnt


for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())

    data = [list(map(int, input().split())) for _ in range(N)]

    start = (R, C)

    visited = [[0 for _ in range(M)] for _ in range(N)]

    ans = bfs(start)

    print("#{} {}".format(tc, ans))
