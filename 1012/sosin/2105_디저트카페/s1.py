import sys
sys.stdin = open('input.txt')
def bfs(u,v,k,cnt):
    global stop, max_cnt
    if k == 3 and (u,v) == stop:
        max_cnt = max(max_cnt, cnt)
    elif not 0 <= u < N or not 0 <= v < N:
        return
    elif area[u][v] in queue:
        return
    else:
        queue.append(area[u][v])
        nx, ny = u + dx[k], v + dy[k]
        if k != 3:
            bfs(nx, ny, k, cnt+1)  # 쭉 그대로 진행
            bfs(u + dx[k+1], v + dy[k+1], k+1, cnt +1) # 방향 전환
        else:
            bfs(nx, ny, k, cnt+1)
        queue.remove(area[u][v])

for T in range(int(input())):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = -1
    dx = [1,1,-1,-1]
    dy = [1,-1,-1,1]
    queue = []
    for i in range(N):
        for j in range(1, N - 1):
            stop = (i,j)
            queue.append(area[i][j])
            bfs(i+1,j+1,0,1)
            queue.remove(area[i][j])

    print('#{} {}'.format((T+1), max_cnt))
#1 6
#2 -1
#3 4
#4 4
#5 8
#6 6
#7 14
#8 12
#9 18
#10 30
