# 바이러스
import sys
sys.stdin = open('input.txt')

def dfs(s):
    global cnt
    visited[s] = 1
    cnt += 1

    for i in range(1, V+1):
        if not visited[i] and G[s][i] == 1:
            dfs(i)

V = int(input())
E = int(input())
G = [[0 for _ in range(V+1)] for _ in range(V+1)]
visited = [0] * (V+1)
cnt = -1

for _ in range(E):
    s, e = map(int, input().split())
    G[s][e] = 1
    G[e][s] = 1

dfs(1)
print(cnt)
