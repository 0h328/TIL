def dfs(start, data):
    stack = [start]
    visited = []
    while stack:
        r, c = stack.pop()          # 방문을 위해 꺼내서
        visited.append((r, c))      # 방문 체크
        for i in range(4):          # 4방향 탐색
            nr = r + dr[i]          # 이동
            nc = c + dc[i]
            move = (nr, nc)
            if 0 <= nr < N and 0 <= nc < N:     # 범위 체크
                if data[nr][nc] == 3:           # 도착지면 종료
                    return 1
                if data[nr][nc] == 0 and move not in visited:   # 갈 수 있는 곳인데 아직 안갔으면
                    stack.append(move)                          # stack에 넣자
    return 0                                                    # 도착지를 못만나고 stack이 빈 경우는 못가는 것을 의미

def find_start(data, N):
    for r in range(N):
        for c in range(N):
            if data[r][c] == 2:
                return r, c

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    start = find_start(data, N)
    ans = dfs(start, data)
    print('#{} {}'.format(tc, ans))