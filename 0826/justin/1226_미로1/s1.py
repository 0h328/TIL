def bfs(r, c):
    Q = [(r, c)]                                     # Q에 넣고
    while Q:
        cur_r, cur_c = Q.pop(0)                      # 해당 위치 뽑아서
        for i in range(4):                           # 4방 이동
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
            if (0 <= nr < N) and (0 <= nc < N):  # 벽을 체크하고
                if data[nr][nc] == 3:                # 도착지점이면
                    return 1                         # 1 반환
                if not data[nr][nc]:                 # 도착지점이 아니지만 갈 수 있는 곳이면
                    Q.append((nr, nc))               # Q에 넣고
                    data[nr][nc] = 1                 # 벽으로 만들어 다시 돌아오지 않도록 처리
    return 0                                         # 루프가 끝났음에도 return을 못 만나면 못가는 것으로 처리

import sys
sys.stdin = open('input.txt')
for _ in range(10):
    tc = int(input())
    N = 16                          # 16 * 16
    data = [list(map(int, input())) for _ in range(N)]
    dr = [-1, 1, 0, 0]              # 방향 델타
    dc = [0, 0, -1, 1]
    for r in range(N):              # 시작점 찾기
        for c in range(N):
            if data[r][c] == 2:     # 찾으면
                ans = bfs(r, c)     # 탐색 시작
    print('#{} {}'.format(tc, ans))