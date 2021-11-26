def DFS(r, c):
    global result
    for m in range(4):                  # 네방향 탐색
        nr, nc = r + dr[m], c + dc[m]
        if 0 <= nr < N and 0 <= nc < N:
            if maze[nr][nc] == 3:       # 만약 이동한 곳에서 도착지를 바로 만나면
                result = 1              # 그대로 종료
                return
            if not maze[nr][nc] and not visited[nr][nc]:    # 이동한 위치가 통로(0) & 방문하지 않은 곳이라면
                visited[nr][nc] = 1     # 방문처리 하고
                DFS(nr, nc)             # 해당 위치에서 재귀적으로 다시 탐색 시작

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    result = 0
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                start_r, start_c = r, c
                DFS(start_r, start_c)

    print('#{} {}'.format(tc, result))