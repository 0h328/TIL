import sys
sys.stdin = open('input.txt')

from collections import deque

dr = [0,0,-1,1]
dc = [1,-1,0,0]
for T in range(int(input())):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start_pos = (i, j)
            elif arr[i][j] == 3:
                er, ec = i, j

    q = deque([[*start_pos, 1]])
    while q:
        r, c, cnt = q.popleft()
        visited[r][c] = cnt

        for k in range(4):
            nr, nc = r+dr[k], c+dc[k]
            if 0<=nr<N and 0<=nc<N and not visited[nr][nc] and arr[nr][nc]!=1:
                q.append([nr, nc, cnt+1])
    answer = visited[er][ec]-2 if visited[er][ec] else visited[er][ec]
    print('#{} {}'.format((T+1), answer))

#1 5
#2 5
#3 0