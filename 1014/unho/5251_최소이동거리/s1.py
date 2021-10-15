import sys
import heapq
sys.stdin = open('input.txt')

# dijkstra heapq
def dijkstra():
    heap = [(0, 0)]

    while heap:
        print(heap)
        w, e = heapq.heappop(heap)
        if not visited[e]:
            visited[e] = 1
            distance[e] = w
            for i in linked[e]:
                if not visited[i[1]]:
                    heapq.heappush(heap, (distance[e]+i[0], i[1]))

T = int(input())
answer = []

for tc in range(1, T+1):
    N, E = map(int, input().split())
    distance = [1e10] * (N+1)
    visited = [0] * (N+1)
    linked = {i:[] for i in range(N+1)}

    for _ in range(E):
        s, e, w = map(int, input().split())
        linked[s].append((w, e))

    dijkstra()

    answer.append('#{} {}'.format(tc, distance[N]))
print(*answer, sep='\n')


# dijkstra default
# def dijkstra():
#     for _ in range(N+1):
#         min_idx = -1
#         min_value = 1e10

#         for i in range(N+1):
#             if not visited[i] and distance[i] < min_value:
#                 min_idx = i
#                 min_value = distance[i]
#         visited[min_idx] = 1

#         for e in linked[min_idx]:
#             if not visited[e[1]] and distance[e[1]] > distance[min_idx] + e[0]:
#                 distance[e[1]] = distance[min_idx] + e[0]


# T = int(input())
# answer = []

# for tc in range(1, T+1):
#     N, E = map(int, input().split())
#     linked = {i:[] for i in range(N+1)}
#     distance = [1e10] * (N+1)
#     distance[0] = 0
#     visited = [0] * (N+1)

#     for _ in range(E):
#         s, e, w = map(int, input().split())
#         linked[s].append((w, e))

#     dijkstra()

#     answer.append('#{} {}'.format(tc, distance[N]))
# print(*answer, sep='\n')