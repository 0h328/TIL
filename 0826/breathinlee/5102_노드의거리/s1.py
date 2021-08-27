import sys
sys.stdin = open('input.txt')

def bfs(S, G):
    q = []                                           # 큐 생성
    visited = [0] * (V+1)                            # visited 생성
    q.append(S)                                      # 시작점 큐에 추가
    visited[S] = 1                                   # 시작점 방문처리

    while q:                                         # q가 빌 때까지 반복
        t = q.pop(0)
        for i in adjList[t]:                         # t에 인접하고
            if i == G:
                return visited[t]
            if visited[i] == 0:                      # 방문하지 않았다면
                q.append(i)                          # q에 추가시키고
                visited[i] = visited[t] + 1          # 방문처리
    return 0



T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjList = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        adjList[u].append(v)
        adjList[v].append(u)
    S, G = map(int, input().split())                            # S : 출발노드, G : 도착노드

    print('#{} {}'.format(tc, bfs(S, G)))