import sys
sys.stdin = open('input.txt')

T = int(input())

def dfs(start):
    stack = [start]
    visited[start[0]][start[1]] = 1

    while stack:
        cur_row, cur_col = stack.pop()

        for i in range(4):
            nxt_row = cur_row + dr[i]
            nxt_col = cur_col + dc[i]
            if 0 <= nxt_row < N and 0 <= nxt_col < N and not visited[nxt_row][nxt_col] and data[nxt_row][nxt_col] != '1':
                if data[nxt_row][nxt_col] == '3':
                    return 1
                stack.append([nxt_row, nxt_col])
                visited[nxt_row][nxt_col] = 1

    return 0


for tc in range(1, T+1):
    N = int(input())
    data = [list(input()) for _ in range(N)]

    #시작 위치 탐색
    for row in range(N):
        for col in range(N):
            if data[row][col] == '2':
                start = [row, col]
                break

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    visited = [[0] * N for _ in range(N)]

    ans = dfs(start)

    print('#{} {}'.format(tc, ans))
