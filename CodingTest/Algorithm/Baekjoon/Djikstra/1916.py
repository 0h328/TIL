import sys
from heapq import heappush, heappop
sys.stdin = open('input.txt')
input = sys.stdin.readline
INF = 999999

def dijkstra(start):
    cost[start] = 0 # 시작지점 비용은 0
    heap = []
    heappush(heap, (0, start))

    while heap:
        end_cost, node = heappop(heap)
        if cost[node] < end_cost:
            continue
        for end_e, c in bus[node]:  # e: 도착지점, c: 비용
            if cost[end_e] > c + end_cost:
                cost[end_e] = c + end_cost
                heappush(heap, (cost[end_e], end_e))

    return cost[end]

N = int(input())    # 도시
M = int(input())    # 버스
bus = [[] for _ in range(N+1)]  # 버스 경로
cost = [INF] * (N+1)            # 비용 리스트
for _ in range(M):
    s, e, w = map(int, input().split()) # s: 출발, e: 도착, w: 비용
    bus[s].append((e, w))

start, end = map(int, input().split())  # start: 출발지, end: 도착지
print(dijkstra(start))

