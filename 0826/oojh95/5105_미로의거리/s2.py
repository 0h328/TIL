import sys
sys.stdin = open('input.txt')

def bfs(r, c):
    global result
    Q.append((r, c))    # 초기 지점에 대해 추가하고 방문했음을 표현
    visited[r][c] = 1

    while Q:    #큐를 다 비우는 동안 진행
        r, c = Q.pop(0)
        for k in range(4):  # 시점으로 부터 이동할 수 있는 공간을 큐로 다 저장해줌.
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc <N:
                if maze[nr][nc] != 1 and visited[nr][nc] == 0:
                    Q.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1

                    if maze[nr][nc] == 3:
                        result = visited[r][c] - 1
                        return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)] # 이동 거리를 표기하기 위해 미로만큼 방문지 기록 행렬 표현

    Q = []
    dr = [-1, 0, 1, 0]  # 이동을 표현하기 위한 델타 표현
    dc = [0, 1, 0, -1]
    result = 0
    for i in range(N):  # 시작점을 찾기위한 기작
        for j in range(N):
            if maze[i][j] == 2:
                start_row = i
                start_col = j

    bfs(start_row, start_col)

    print(visited)

    print('#{} {}'.format(tc, result))