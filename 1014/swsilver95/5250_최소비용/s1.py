import sys
from heapq import *
sys.stdin = open('input.txt', 'r')


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


T = int(input())


def dijkstra(r, c):
    distance[r][c] = 0
    heap = []
    heappush(heap, (0, r, c))

    while heap:
        dist, row, col = heappop(heap)

        for d in range(4):
            nr = row + dr[d]
            nc = col + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if data[nr][nc] > data[row][col]:
                    next_dist = data[nr][nc] - data[row][col] + 1
                else:
                    next_dist = 1

                # next_dist = max(0, data[nr][nc] - data[row][col]) + 1
                total_dist = dist + next_dist
                if distance[nr][nc] > total_dist:
                    distance[nr][nc] = total_dist
                    heappush(heap, (total_dist, nr, nc))


for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    INF = 100001
    distance = [[INF] * N for _ in range(N)]
    dijkstra(0, 0)
    # print(distance)
    print('#{} {}'.format(tc, distance[N - 1][N - 1]))

