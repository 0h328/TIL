import sys
sys.stdin = open('input.txt')

def dijkstra():
    for _ in range(V):
        min_idx = -1                                                        # 최소 인덱스 & 값 초기화
        min_value = 987654321
        for i in range(V+1):                                                # 최솟값 & 그때의 인덱스 찾기
            if not visited[i] and min_value > dist[i]:                      # 아직 i정점에 방문하지 않았고 dist[i]가 최솟값보다 작은 경우
                min_idx = i                                                 # 최솟값 인덱스 갱신
                min_value = dist[i]                                         # 최솟값 갱신
        visited[min_idx] = 1                                                # 최종 최솟값 갱신 후 방문처리

        for j in range(V+1):                                                # 인접 행렬에서 min_idx의 인접인 정점 중에서 최소 거리 갱신
            if not visited[j] and dist[j] > dist[min_idx] + G[min_idx][j]:

                dist[j] = dist[min_idx] + G[min_idx][j]
    return dist[V]

for tc in range(int(input())):
    n = int(input())
    zone = [list(map(int, input().split())) for _ in range(n)]
    G = [[987654321 for _ in range(n+1)] for _ in range(n+1)]
    dist = [987654321] * (n+1)                                     # 비용(거리) 초기화
    dist[0] = 0                                                    # 시작 정점 지점 (0번 -> 0번의 거리는 0)
    visited = [0] * (n+1)                                          # 방문 체크
    for _ in range(n):
        start, end, w = map(int, input().split())                  # 유향(방향있는) 그래프
        G[start][end] = w                                          # 시작 / 끝 / 가중치(길이)
    print(dijkstra())
'''
def bfs(row, col, cnt):
    que = deque()
    que.append((row, col, cnt))
    visited[row][col] = 1
    while que:
        row, col, cnt = que.popleft()
        for i in range(2):
            nrow = row + dr[i]
            ncol = col + dr[i]
            if 0 <= nrow < n and 0 <= ncol < n and not visited[nrow][ncol]:
                if visited[nrow][ncol] - visited[row][col] > 0:
                    que.append((nrow, ncol, cnt + visited[nrow][ncol] - visited[row][col] + 1))
                else:
                    que.append((nrow, ncol, cnt + 1))

for tc in range(int(input())):
    n = int(input())
    zone = [list(map(int, input().split())) for _ in range(n)]
    dr = [1, 0]
    dc = [0, 1]
    visited = [[0]*n for i in range(n)]
    bfs(0, 0, 0)
'''