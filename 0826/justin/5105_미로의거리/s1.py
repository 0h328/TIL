def bfs(r, c):
    Q = []
    Q.append((r, c))    # 좌표 정보 넣기
    visited[r][c] = 1   # 동시에 방문 처리
    while Q:
        r, c = Q.pop(0)
        for i in range(4):                      # 4방 이동
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:     # 범위 체크
                if data[nr][nc] == 3:           # 출구를 만난 경우 지금까지 지나온 칸 반환
                    return visited[r][c] - 1    # 마지막 도착지 직전까지 확인(1로 체크를 시작하니 최종적으로 도착지 - 1)
                elif data[nr][nc] == 0 and not visited[nr][nc]:    # 갈 수 있는 곳이고 아직 그곳에 방문하지 않았다면
                    Q.append((nr, nc))                   # 큐에 넣고
                    visited[nr][nc] = visited[r][c] + 1  # 방문 처리(거리 정보 누적)
    return 0                                             # 출구(3)에 가지 못하고 모든 칸 방문

def find_start(data):
    for r in range(N):
        for c in range(N):
            if data[r][c] == 2:
                return r, c

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())                                        # 미로 크기
    data = [[int(i) for i in input()] for _ in range(N)]    # 미로 정보
    visited = [[0 for _ in range(N)] for _ in range(N)]     # 방문 체크
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    sr, sc = find_start(data)                               # 시작 좌표 찾기
    ans = bfs(sr, sc)
    print('#{} {}'.format(tc, ans))