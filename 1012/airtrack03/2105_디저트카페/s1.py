T = int(input())


# 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래
dr = [-1, -1, 1, 1]
dc = [-1, 1, -1, 1]

nds = {0: [0, 2], 1: [1, 0], 2: [2, 3], 3: [3, 1]}  # 반시계 방향 기준


def dfs(start, d, d_chk):
    global ans
    while stack:
        cur_row, cur_col = stack.pop()
        nxt_row = cur_row + dr[d]
        nxt_col = cur_col + dc[d]

        if 0 <= nxt_row < N and 0 <= nxt_col < N:
            if nxt_row == start[0] and nxt_col == start[1]:
                if ans < visited[cur_row][cur_col] + 1:
                    ans = visited[cur_row][cur_col] + 1
                return
            if not chk[data[nxt_row][nxt_col]] and visited[nxt_row][nxt_col] == -1:
                for nd in nds[d]:
                    if d != nd:
                        if d_chk[nd]:
                            continue
                        d_chk[d] = 1
                    temp = visited[nxt_row][nxt_col]
                    visited[nxt_row][nxt_col] = visited[cur_row][cur_col] + 1
                    chk[data[nxt_row][nxt_col]] = 1
                    stack.append((nxt_row, nxt_col))
                    temp_d_chk = d_chk[:]
                    dfs((nxt_row, nxt_col), start, nd, d_chk)
                    visited[nxt_row][nxt_col] = temp
                    chk[data[nxt_row][nxt_col]] = 0
                    d_chk = temp_d_chk[:]


for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    ans = -1

    for row in range(N):
        for col in range(1, N - 1):
            for i in range(4):
                visited = [[-1] * N for _ in range(N)]
                chk = [0] * 101
                stack = [(row, col)]
                visited[row][col] += 1
                chk[data[row][col]] = 1
                d_chk = [0, 0, 0, 0]

                dfs((row, col), i, d_chk)
    print("#{} {}".format(tc, ans))
