import sys
import heapq
sys.stdin = open('input.txt')


def dijkstra():
    heap = [(0, (0, 0))]

    while heap:
        w, coor = heapq.heappop(heap)
        if not visited[coor[0]][coor[1]]:
            visited[coor[0]][coor[1]] = 1
            distance[coor[0]][coor[1]] = w
            for k in range(4):
                r = coor[0] + dr[k]
                c = coor[1] + dc[k]

                if 0 <= r < N and 0 <= c < N and not visited[r][c]:
                    if distance[r][c] > distance[coor[0]][coor[1]] + int(land[r][c]):
                        heapq.heappush(heap, (distance[coor[0]][coor[1]] + int(land[r][c]), (r, c)))


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())
answer = []

for tc in range(1, T+1):
    N = int(input())
    land = [list(input()) for _ in range(N)]
    
    distance = [[1e8 for _ in range(N)] for _ in range(N)]
    visited = [[0] * N for _ in range(N)]


    dijkstra()
    answer.append('#{} {}'.format(tc, distance[N-1][N-1]))

print(*answer, sep='\n')