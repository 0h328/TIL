def prim():
    for _ in range(V):                                             # 정점 수만큼 반복을 돌며
        min_idx = -1
        min_value = 987654321                                      # 최솟값을 가진 인덱스 찾기
        for i in range(V+1):                                       # 인접 행렬이기 때문에 전체를 돌면서 확인
            if not visited[i] and key[i] < min_value:              # i번째 정점을 선택하지 않았고 선택하지 않은 정점 중에서 가장 작은 값이라면
                min_idx = i                                        # 최솟값 인덱스 초기화
                min_value = key[i]                                 # 최솟값 초기화
        visited[min_idx] = 1                                       # 해당 정점 방문 처리
        for i in range(V+1):                                       # 인접 행렬 돌면서 -> 갱신이 가능하다면 갱신
            if not visited[i] and G[min_idx][i] < key[i]:          # 정점 선택 안했고 해당 가중치가 key의 요소보다 작으면
                key[i] = G[min_idx][i]                             # 가중치 갱신
    return sum(key)                                                # 최종 간선의 가중치

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())                               # V개의 정점 -> 0부터 시작하기 때문에 개수는 +1
    G = [[987654321 for _ in range(V + 1)] for _ in range(V + 1)]  # 임의의 큰 값(무한대)으로 초기화
    key = [987654321] * (V + 1)                                    # 갱신된 최솟값 가중치(처음은 무한대 초기화) -> MST에 포함되는 비용
    key[0] = 0                                                     # 0번 정점을 시작 정점으로 선택
    visited = [0] * (V + 1)                                        # 현재 정점을 사용(선택)했는지 여부 체크
    for i in range(E):
        start, end, W = map(int, input().split())                  # start, end, W: 가중치
        G[start][end] = G[end][start] = W                          # 무향 그래프
    ans = prim()
    print('#{} {}'.format(tc, ans))