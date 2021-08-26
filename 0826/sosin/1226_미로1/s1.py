import sys
sys.stdin = open('input.txt')

from collections import deque

dr = [0,0,-1,1]
dc = [1,-1,0,0]
for T in range(1, 11):
    input()

    arr = [list(map(int, input())) for _ in range(16)]
    visited = [[0]*16 for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                start_pos = (i, j)
            elif arr[i][j] == 3:
                er, ec = i, j

    q = deque([start_pos])
    while q:
        r, c = q.popleft()
        visited[r][c] = 1

        for k in range(4):
            nr, nc = r+dr[k], c+dc[k]
            if 0<=nr<16 and 0<=nc<16 and not visited[nr][nc] and arr[nr][nc]!=1:
                q.append((nr, nc))
        
    print('#{} {}'.format((T), visited[er][ec]))


#1 1
#2 1
#3 1
#4 0
#5 1
#6 1
#7 0
#8 1
#9 1
#10 1
