def dijkstra():
    Q = []  # 소비량이 갱신된 지역의 인접 지역 저장
    dist[0][0] = 0                                                # 시작점은 0으로 초기화
    Q.append((0, 0))
    while Q:                                                      # 더이상 갱신되는 경우가 없을 때까지 반복
        r, c = Q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                diff = 0
                if arr[nr][nc] > arr[r][c]:                       # 가려는 곳이 더 높다면
                    diff = arr[nr][nc] - arr[r][c]                # 높이 차이 계산
                if dist[nr][nc] > (dist[r][c] + diff + 1):        # 기존 비용보다 이동 비용이 적으면
                    dist[nr][nc] = dist[r][c] + diff + 1          # 비용 갱신
                    Q.append((nr, nc))                            # 주변도 갱신될 수 있으므로 저장
    return dist[N-1][N-1]

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    dist = [[987654321] * N for i in range(N)]                    # 각 칸 까지의 최소 연료 소비량
    arr = [list(map(int, input().split())) for i in range(N)]     # 각 지역의 높이 정보
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    ans = dijkstra()
    print('#{} {}'.format(tc, ans))