import sys
import heapq
sys.stdin = open('input.txt')

# dijkstra heapq
def dijkstra():
    heap = [(0, 0, 0)]

    while heap:
        w, y, x = heapq.heappop(heap)
        if not visited[y][x]:
            visited[y][x] = 1
            distance[y][x] = w
            for k in range(4):
                r = y + dr[k]
                c = x + dc[k]

                if 0 <= r < N and 0 <= c < N and not visited[r][c]:
                    weight = land[r][c] - land[y][x] + 1
                    if weight < 1:
                        weight = 1
                    heapq.heappush(heap, (distance[y][x]+weight, r, c))


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())
answer = []

for tc in range(1, T+1):
    N = int(input())
    land = [list(map(int, input().split())) for _ in range(N)]
    distance = [[1e10] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    dijkstra()

    answer.append('#{} {}'.format(tc, distance[N-1][N-1]))
print(*answer, sep='\n')



# dijkstra default timeout
'''
def dijkstra():
    for _ in range(N*N):
        min_r = -1
        min_c = -1
        min_value = 1e10

        for i in range(N):
            for j in range(N):
                if not visited[i][j] and min_value > distance[i][j]:
                    min_r = i
                    min_c = j
                    min_value = distance[i][j]
        visited[min_r][min_c] = 1

        for k in range(4):
            r = min_r + dr[k]
            c = min_c + dc[k]

            if 0 <= r < N and 0 <= c < N and not visited[r][c]:
                weight = land[r][c] - land[min_r][min_c] +1
                if weight < 1:
                    weight = 1
                if distance[r][c] > distance[min_r][min_c] + weight:
                    distance[r][c] = distance[min_r][min_c] + weight
    

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())
answer = []

for tc in range(1, T+1):
    N = int(input())
    land = [list(map(int, input().split())) for _ in range(N)]
    distance = [[1e10] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    distance[0][0] = 0

    dijkstra()
    
    answer.append('#{} {}'.format(tc, distance[N-1][N-1]))
print(*answer, sep='\n')
'''