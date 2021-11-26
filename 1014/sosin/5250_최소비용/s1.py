import sys
sys.stdin = open('input.txt')

dr = [1,0]
dc = [0,1]
from collections import deque

for T in range(int(input())):
    result = 0
    N = int(input())
    graph = [tuple(map(int, input().split())) for _ in range(N)]
    INF = 1e9
    visited = [[INF]*N for _ in range(N)]

    start_pos = [0,0]
    q = deque([start_pos])
    visited[0][0] = 0
    while q:
        r, c = q.popleft()
        for k in range(2):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0<=nr<N and 0<=nc<N:
                if visited[nr][nc] != INF:
                    temp = visited[nr][nc]
                    visited[nr][nc] = min(visited[nr][nc], visited[r][c] + 1 + max(0, graph[nr][nc]-graph[r][c]))
                    if temp == visited[nr][nc]:
                        continue
                else:
                    visited[nr][nc] = visited[r][c] + 1 + max(0, graph[nr][nc]-graph[r][c])
                q.append((nr, nc))
    print(*visited, sep='\n')
    
    print('#{} {}'.format((T+1), visited[N-1][N-1]))

#1 5
#2 8
#3 9