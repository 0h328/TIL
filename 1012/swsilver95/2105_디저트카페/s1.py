import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


dx = [-1, -1, 1, 1]     # 왼쪽 위, 오른쪽 위, 오른쪽 아래, 왼쪽 아래
dy = [-1, 1, 1, -1]

# 방향전환을 세 번만 해야 됨


def dfs(r, c, selected, direction, direction_cnt, length):
    global row, col, answer
    if r == row and c == col and direction_cnt == 4:
        if answer < length:
            answer = length
        return

    for d in range(4):
        nx = r + dx[d]
        ny = c + dy[d]
        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny] and cafe[nx][ny] not in selected:
                visited[nx][ny] = True
                selected.append(cafe[nx][ny])
                if d != direction:
                    dfs(nx, ny, selected, d, direction_cnt + 1, length + 1)
                else:
                    dfs(nx, ny, selected, d, direction_cnt, length + 1)
                visited[nx][ny] = False
                selected.pop()


for tc in range(1, T + 1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    answer = -1

    for row in range(N):
        for col in range(N):
            visited[row][col] = True
            dfs(row, col, [], -1, 0, 0)
            visited[row][col] = False

    print('#{} {}'.format(tc, answer))