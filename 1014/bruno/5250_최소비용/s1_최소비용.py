import sys
from collections import deque
sys.stdin = open('input.txt')

for T in range(1, int(input())+1):
    N = int(input())
    road = [list(map(int, input().split())) for _ in range(N)]
    dr = [0, 1, 0, -1]  # 우하좌상
    dc = [1, 0, -1, 0]
    distance = [[987654321]*N for _ in range(N)]    # 비용
    distance[0][0] = 0  # 출발지점 초기화
    queue = deque()
    queue.append((0, 0))
    while queue:
        r, c = queue.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                cnt = 1
                if road[nr][nc] > road[r][c]:
                    cnt += road[nr][nc] - road[r][c]
                if distance[nr][nc] > distance[r][c] + cnt:
                    distance[nr][nc] = distance[r][c] + cnt
                    queue.append((nr, nc))
    print('#{} {}'.format(T, distance[N-1][N-1]))
