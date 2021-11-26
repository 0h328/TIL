import sys
sys.stdin = open('input.txt')

dr = [0,0,-1,1]
dc = [1,-1,0,0]

def dfs(r, c):
    global result, first
    Q = [(r, c, 1)]
    while Q:
        tr, tc, cnt = Q.pop()
        for k in range(4):
            nr = tr+dr[k]
            nc = tc+dc[k]
            if 0<=nr<N and 0<=nc<N and maps[nr][nc] - maps[tr][tc] == 1 and not visited[nr][nc]:
                Q.append((nr, nc, cnt+1))
                break
        else:
            if result < cnt:
                result = cnt
                first = maps[tr][tc] - cnt + 1

for T in range(int(input())):
    result = 0
    first = 0
    N = int(input())
    maps =[list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    coord_list = [(0, 0)] * (N*N+1)

    for i in range(N):
        for j in range(N):
            coord_list[maps[i][j]] = (i, j)

    for i, j in coord_list[1:]:
        visited[i][j] = 1
        dfs(i, j)
        
    print('#{} {} {}'.format((T+1), first, result))

#1 6 8
#2 3 2
#3 149 2
#4 2 45
#5 2 23
#6 1 2
#7 1 4
#8 5 17
#9 4 2
#10 1 35
#11 2 2
#12 7 2
#13 45 2
#14 113 2
#15 12 32
#16 6 9
#17 1 4
#18 36 42
#19 204 2
#20 7 14
#21 4 2
#22 8225 2200
#23 35 3
#24 2 2
#25 613 2
#26 33 2
#27 5 5
