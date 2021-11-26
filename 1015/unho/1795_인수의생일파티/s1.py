'''
다익스트라를 한번만 돌고 해결할수는 없을까??
'''


import sys
import heapq
sys.stdin = open('input.txt')

def dijkstra(w, e, stop):
    global distance

    distance = [0] * (N+1)
    visited = [0] * (N+1)

    heap = [(w, e)]
    
    while heap and not visited[stop]:
        w, v = heapq.heappop(heap)
        if not visited[v]:
            visited[v] = 1
            distance[v] = w

            if visited[stop]:           # 원하는 구역 도착시 종료
                return distance[stop]

            for i in linked[v]:
                if not visited[i[1]]:
                    heapq.heappush(heap, (distance[v]+i[0], i[1]))


T = int(input())
answer = []

for tc in range(1, T+1):
    N, M, X = map(int, input().split())     # 집의 총 개수 / 도로 개수 / 목적지 집
    linked = {i:[] for i in range(N+1)}
    tc_answer = 0

    for _ in range(M):
        x, y, c = map(int, input().split())
        linked[x].append((c, y))

    dijkstra(0, X, 0)
    go_distance = distance[:]

    for i in range(1, N+1):
        if i != X:
            back = dijkstra(0, i, X)
            if tc_answer < back + go_distance[i]:
                tc_answer = back + go_distance[i]
    
    answer.append('#{} {}'.format(tc, tc_answer))

print(*answer, sep='\n')