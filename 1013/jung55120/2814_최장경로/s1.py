import sys
sys.stdin = open('input.txt')

def dfs(idx, cnt):
    global result

    if cnt > result:
        result = cnt

    for i in road[idx]:
        if not visited[i]:
            visited[i] = 1
            dfs(i, cnt+1)
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    road = [[] for _ in range(N+1)]
    # print(road)
    result = 1
    visited = [0] * (N+1)
    for i in range(M):
        x, y = map(int, input().split())
        road[x].append(y)
        road[y].append(x)

    for j in range(1, len(road)):
        visited[j] = 1
        dfs(j, 1)
        visited[j] = 0

    print('#{} {}'.format(tc, result))