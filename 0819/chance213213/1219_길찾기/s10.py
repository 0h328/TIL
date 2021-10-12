import sys
sys.stdin = open('input.txt')

def dfs(v):
    global ans
    if v == 99:
        ans = 1
    visited[v] = 1
    for w in G[v]:
        if not visited[w]:
            dfs(w)



for _ in range(10):
    tc, E = map(int, input().split())
    temp = list(map(int, input().split()))
    G = [[] for _ in range(100)]
    for i in range(E):
        G[temp[2*i]].append(temp[2*i+1])
    visited = [0 for _ in range(100)]
    ans = 0
    dfs(0)
    print('#{} {}'.format(tc, ans))