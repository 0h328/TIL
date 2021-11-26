# DFS와 BFS
from collections import deque
import sys
sys.stdin = open('input.txt')

def dfs(s):
    visited[s] = 1
    print(s, end=' ')
    for i in range(1, N+1):
        if G[s][i] == 1 and not visited[i]:
            dfs(i)

def bfs(s):
    q = deque()
    q.append(s)
    visited[s] = 1
    
    while q:
        t = q.popleft()
        print(t, end=' ')        
        
        for i in range(1, N+1):
            if not visited[i] and G[t][i] == 1:
                q.append(i)
                visited[i] = 1
    

N, M, V = map(int, input().split())
G = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    s, e = map(int, input().split())
    G[s][e] = 1
    G[e][s] = 1

dfs(V)
visited = [0] * (N+1)
print()
bfs(V)

