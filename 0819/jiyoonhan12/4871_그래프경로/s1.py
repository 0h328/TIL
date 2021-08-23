import sys
sys.stdin = open('input.txt')

def findRoot(depart): # dfs
    if not visited[depart]:
        visited[depart] = 1

    for node in range(1, V+1):
        if graph[depart][node] == 1 and not visited[node]:
            findRoot(node)


T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[0] * (V+1) for _ in range(V+1)]

    for _ in range(E): # 간선 정보 기록
        td, ta = map(int, input().split())
        graph[td][ta] = 1

    depart, arrive = map(int, input().split()) # 출발지, 도착지

    visited = [0 for _ in range(V+1)]

    findRoot(depart) # 출발지 기준으로 dfs 돌고 나서

    if visited[arrive]: # arrive에 방문한 적 있다 = root 있음
        res = 1
    else:
        res = 0
    print('#{} {}'.format(t, res))