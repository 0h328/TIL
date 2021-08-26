import sys
sys.stdin = open('input.txt')

def bfs(S, G):
    q = [0] * V                                      # 큐 생성
    front = rear = -1
    visited = [0] * (V+1)                            # visited 생성
    rear += 1
    q[rear] = S
    visited[S] = 1                                   # 시작노드 방문처리

    while front != rear:                             # 큐가 비어있지 않으면




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