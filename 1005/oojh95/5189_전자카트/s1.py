import sys
sys.stdin = open('input.txt')

def bfs(r,c):
    global result
    Q.append(r, c)
    visited[s] += 1

    while Q:
        s = Q.pop(0)
        for i in range(1, V+1):
            if num[s][i] and not visited[i]:
                Q.append(i)
                visited[i] = 1
                distance[i] = distance[s] + 1
                if i == G:
                    result = distance[i]
                    return
    return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0*(N+1)]
    Q = []
    for j in range(2, N):
        bfs(1, j)
