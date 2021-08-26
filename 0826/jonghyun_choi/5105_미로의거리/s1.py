import sys
sys.stdin = open('input.txt')

T = int(input())

dr = [0,0,1,-1]
dc = [1,-1,0,0]

def BFS(graph, i, j):
    q = []
    q.append((i,j))
    while q:
        r, c = q.pop(0)
        for k in range(4):
            next_r = r + dr[k]
            next_c = c + dc[k]
            if 0 <= next_r < N and 0 <= next_c < N and graph[next_r][next_c] != '1':
                if graph[next_r][next_c] == '3':
                    visited[next_r][next_c] = visited[r][c] + 1
                    return visited[next_r][next_c] - 1
                elif graph[next_r][next_c] == '0':
                    graph[next_r][next_c] = '1'
                    visited[next_r][next_c] = visited[r][c] + 1
                    q.append((next_r,next_c))
    return 0






for case in range(T):
    N = int(input())
    data = [list(map(str, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if data[i][j] == '2':
                print('#{} {}'.format(case+1, BFS(data, i, j)))
