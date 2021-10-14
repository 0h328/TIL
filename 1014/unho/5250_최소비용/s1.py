import sys
import heapq
sys.stdin = open('input.txt')


def dijkstra():
    heap = []
    heapq.heappush(heap, (0, 0, 0))     # 가중치 / y / x

    while heap:
        w, y, x = heapq.heappop(heap)
        if not visited[y][x]:
            visited[y][x] = 1
            dist[y][x] = w
            
            for i in range(N):
                for j in range(N):
                    if not visited[i][j]:
                        heapq.heappush(heap, dist[y][x]+linked[i][j][2], i, j)
    
    return dist[N-1][N-1]


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())
answer = []

for tc in range(1, T+1):
    N = int(input())
    land = [list(map(int, input().split())) for _ in range(N)]
    linked = [[[] for j in range(N)] for i in range(N)]
    visited = [[0] * N for _ in range(N)]
    dist = [[1e10] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(4):
                r = i + dr[k]
                c = j + dc[k]

                if 0 <= r < N and 0 <= c < N:
                    linked[i][j].append([r, c, land[r][c]-land[i][j]])

    print(linked)
    print(dijkstra())



# def dfs(y, x, ans):
#     global tc_answer

#     if y == N-1 and x == N-1:
#         if ans < tc_answer:
#             tc_answer = ans
#         return
#     elif ans >= tc_answer:
#         return

#     for k in range(4):
#         r = y + dr[k]
#         c = x + dc[k]

#         if 0 <= r < N and 0 <= c < N and not visited[r][c]:
#             visited[r][c] = 1

#             if land[r][c] > land[y][x]:
#                 dfs(r, c, ans+land[r][c]-land[y][x]+1)
#             else:
#                 dfs(r, c, ans+1)
            
#             visited[r][c] = 0


# dr = [-1, 0, 1, 0]
# dc = [0, 1, 0, -1]

# T = int(input())
# answer = []

# for tc in range(1, T+1):
#     N = int(input())
#     land = [list(map(int, input().split())) for _ in range(N)]
#     visited = [[0] * N for _ in range(N)]
#     tc_answer = 1e10

#     visited[0][0] = 1
#     dfs(0, 0, 0)

#     answer.append('#{} {}'.format(tc, tc_answer))
# print(*answer, sep='\n')