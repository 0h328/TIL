import sys

sys.stdin = open('input.txt')


def prim():
    for _ in range(V):                                     # 모든 정점이 MST에 포함될 때까지 반복
        min_idx = -1
        min_value = 11
                                                           # key가 최솟값을 갖는 인덱스 찾기
        for i in range(V+1):                               # 인접 행렬이기 때문에 전체를 돌면서 확인
            if not visited[i] and key[i] < min_value:      # i번째 정점을 선택하지 않았고 선택하지 않은 정점 중에서 가장 적은 값이라면
                min_idx = i                                # 최솟값 인덱스 초기화
                min_value = key[i]                         # 최솟값 초기화
        visited[min_idx] = 1                               # 해당 정점 사용 처리

        for i in range(V+1):                               # min_idx와 연결된 인접 행렬 돌면서
            if not visited[i] and G[min_idx][i] < key[i]:  # 정점 선택 안했고 해당 가중치가 key의 요소보다 작으면 (== 더 적은 비용으로 MST에 연결되면)
                key[i] = G[min_idx][i]                     # 가중치 갱신

    return sum(key)                                        # 최종 간선의 가중치

import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    V, E = map(int, input().split())                                # V개의 정점 -> 0부터 시작하기 때문에 개수는 +1
    G = [[11 for _ in range(V+1)] for _ in range(V+1)]       # 임의의 큰 값으로 초기화
    key = [11] * (V+1)                                       # 갱신된 최솟값 가중치(처음은 임의의 큰 값으로 초기화) -> MST에 속하는데 포함되는 비용(가중치)
    key[0] = 0                                                      # 0번 정점을 시작 정점으로 선택 (처음은 가중치가 0)
    visited = [0] * (V+1)                                           # 현재 정점을 선택했는지 여부 체크 (MST에 속하는지 여부)
    for i in range(E):
        start, end, W = map(int, input().split())                   # start, end, W: 가중치
        G[start][end] = W                                           # 무향 그래프이므로 양쪽에 모두 가중치 체크
        G[end][start] = W

    print('#{} {}'.format(t, prim()))