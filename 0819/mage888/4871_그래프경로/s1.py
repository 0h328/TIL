import sys
sys.stdin = open('input.txt')
from pandas import DataFrame

def dfs(depart, arrive):
    stack = [depart]                # 시작 정점 stack에 넣어놓고 시작

    while stack:                    # stack이 빌때까지 while len(stack) 등도 가능
        depart = stack.pop()        # stack의 가장 위에서 정점을 꺼내

        if not visited[depart]:     # 아직 방문하지 않았다면
            visited[depart] = 1     # 방문 체크
            # print('방문 정점: {}, 방문 체크: {}'.format(depart, visited))

            for w in range(1, V+1):                             # 모든 정점에 대한 반복을 수행하며
                if table[depart][w] == 1 and not visited[w]:    # 해당의 인접 정점이고 아직 방문하지 않았다면
                    stack.append(w)
    if visited[arrive]:
        return 1

    return 0

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())        # V(ertex)정점의 개수와 E(dge) 간선의 수를 변수로 표현

    table = [[0 for _ in range(V+1)] for _ in range(V+1)]       # 인접행렬 생성

    for _ in range(E):                                          # 간선의 개수 범위를 돌면서
        depart, arrive = map(int, input().split())              # 출발과 도착
        table[depart][arrive] = 1                               # 단방향

    depart_node, arrive_node = map(int, input().split())        # 출발노드와 도착노드를 변수 S, A로 표현

    visited = [0 for _ in range(V+1)]

# dfs(depart_node)

    print('#{} {}'.format(tc, dfs(depart_node, arrive_node)))