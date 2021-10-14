import sys
import heapq
sys.stdin = open('input.txt')


def prim():
    global ans

    heap = []                       # 최소힙
    heapq.heappush(heap, (0,0))     # 최소힙, 
    
    while heap:
        w, v = heapq.heappop(heap)
        if not visited[v]:
            ans += w
            visited[v] = 1
            for w, weight in linked[v]:
                if not visited[w]:
                    heapq.heappush(heap, (weight, w))
    return ans


T = int(input())
answer = []

for tc in range(1, T+1):
    V, E = map(int, input().split())
    linked = [[] for _ in range(V+1)]       # 인접 리스트
    ans = 0                                 # 누적할 가중치
    visited = [0] * (V+1)                   # 방문여부

    for i in range(E):                      # 연결관계 [연결된 노드, 가중치]
        start, end, W = map(int, input().split())
        linked[start].append([end, W])
        linked[end].append([start, W])
    
    print(linked)

    print('#{} {}'.format(tc, prim()))