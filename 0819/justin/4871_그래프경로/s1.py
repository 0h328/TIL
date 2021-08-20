"""
방향성 그래프
 - 출발 -> 도착
 - 만약 특정한 정점 A에서 출발 했을 때 특정한 정점 B에 도착할 수 있는지 여부를 확인

 테스트 케이스가 어떻게 들어오는지 정확하게 파악해야 함

 3 -> 테스트 케이스 수
 6, 5 -> Vertex(정점), Edge(간선)

 그 다음 줄부터 간선의 개수만큼 출발 & 도착 정점이 주어진다.
 1 4 -> 1번에서 4번 정점으로
 1 3 -> 1번에서 3번 정점으로
 2 3 -> 2번에서 3번 정점으로
 2 5 -> 2번에서 5번 정점으로
 4 6 -> 4번에서 6번 정점으로

 마지막 줄에는 출발 & 도착 정점이 주어진다.
 1 6 -> 1번 정점에서 출발하여 6번 정점으로 갈 수 있는가?
"""

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())             # V(vertex) - 정점, E(edge) - 간선
    G = [[] for _ in range(V+1)]                 # V+1은 인덱스와 정점 번호의 일치를 위함
    for _ in range(E):                           # 간선의 수만큼 반복을 돌며
        s, g = map(int, input().split())         # 출발 & 도착 정점을 받고
        """
        인접 리스트의 활용 
        인덱스 관리의 편의상 0번은 비워두고 아래와 같이 각 정점 별 연결된 인접 정점 확인 가능
           1     2      3    4   5   6
        [4, 3] [3, 5]  [ ]  [6] [ ] [ ]

        방향이 존재하기 때문에 1 -> 4는 가능해도 4 -> 1은 안된다.
        """
        G[s].append(g)                           # s 정점에 해당하는 리스트에 g 정점 추가
    Start, Goal = map(int, input().split())      # S(tart) -> 출발 정점 / G(oal) -> 도착 정점
    visited = [0] * (V+1)                        # 방문 체크 리스트(인덱스 관리를 위해 V+1)
    stack = [Start]                              # 출발 지점을 스택에 넣어놓고 시작

    while stack:                                 # stack이 빌 때까지 반복 (모든 정점 방문 완료)
        v = stack.pop()                          # 먼저 스택에서 정점을 하나 꺼내
        if not visited[v]:                       # 그 정점이 방문하지 않은 정점이라면
            visited[v] = 1                       # 방문 처리를 하고
            for v in G[v]:                       # 해당 정점에 연결된 다른 정점(인접 정점)을 돌며
                if not visited[v]:               # 만약 그 곳이 방문하지 않은 곳이라면
                    stack.append(v)              # stack에 추가
    ans = 1 if visited[Goal] else 0              # 도착해야 하는 곳이 방문을 했던 곳이라면 1 아니라면 0
    print('#{} {}'.format(tc, ans))