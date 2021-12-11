import sys
sys.stdin = open('input.txt')
INF = 1e9
sys.setrecursionlimit(int(INF))
input = sys.stdin.readline

def dfs(s):

    check[s] = 1

    for i in range(s, N+1):
        if not check[i] and G[s][i]:
            dfs(i)

N, M = map(int, input().split())
G = [[0] * (N+1) for _ in range(N+1)]
check = [0] * (N+1)
cnt = 0

for _ in range(M):
    u, v = map(int, input().split())
    G[u][v] = 1
    G[v][u] = 1

for i in range(1, N+1):
    if not check[i]:
        cnt += 1
        dfs(i)

print(cnt)
