import sys
sys.stdin = open('input.txt')

def dfs(pos, cnt):
    global result
    visited[pos] = 1

    for g in graph[pos]:
        if visited[g]:
            result = max(result, cnt)
        else:
            dfs(g, cnt+1)

    visited[pos] = 0

for T in range(int(input())):
    result = 1
    N, M = map(int, input().split())
    data = [tuple(map(int, input().split())) for _ in range(M)]
    graph = {i:[] for i in range(N)}
    for a, b in data:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    
    visited = [0]*N

    for a in range(N):
        dfs(a, 1)
    
    print('#{} {}'.format((T+1), result))

#1 1
#2 3