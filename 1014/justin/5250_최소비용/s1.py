def dijkstra():
    heap = []
    dist[0][0] = 0                                                # 시작점 초기화 -> (0, 0)은 0이라는 비용을 지불하여 갈 수 있는 곳
    heapq.heappush(heap, (dist[0][0], 0, 0))                      # (가중치, 행, 열)

    while heap:                                                   # heap가 비었다?
                                                                  # 경로 자체를 어떻게 갔는지는 모르지만 (0, 0)에서 시작하여 어떤 지점까지 가는데 필요한 최소 비용은 아는 상태
        cur_w, cur_r, cur_c = heapq.heappop(heap)                 # 최소힙 -> 가중치가 작은 순서 부터(가중치가 같다면 행 -> 열 순서)
        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:                       # 범위 체크
                additional_cost = arr[nr][nc] - arr[cur_r][cur_c] # 높이에 따른 연료의 크기 세팅 (다음 좌표 - 현재 좌표 -> 추가적인 연료 소모 여부 확인)
                if additional_cost < 0:                           # 높은 곳 -> 낮은 곳 이동 시에는 추가적인 비용이 없음 (음수가 나오면 0으로 초기화)
                    additional_cost = 0
                new_w = cur_w + 1 + additional_cost               # 새로운 가중치 = 현재 가중치(cur_w) + 기본 이동 값(1) + 높이에 따른 소모량
                if dist[nr][nc] > new_w:                          # 만약 새로 이동한 곳의 값이 새로운 가중치 보다 크면
                    dist[nr][nc] = new_w                          # 새로운 가중치로 초기화하고
                    heapq.heappush(heap, (dist[nr][nc], nr, nc))  # (가중치, 행, 열) 순으로 heappush
    return dist[N-1][N-1]                                         # 도착 지점은 항상 오른쪽 최하단

import sys
import heapq
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    dist = [[987654321] * N for _ in range(N)]                    # 거리 무한대 초기화 (2차원 다익스트라)
    arr = [list(map(int, input().split())) for _ in range(N)]     # 2차원 리스트
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    ans = dijkstra()
    print('#{} {}'.format(tc, ans))