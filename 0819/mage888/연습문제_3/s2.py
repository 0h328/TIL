import sys
sys.stdin = open('input2.txt')

V, E = map(int, input().split())

# G = [[0] * (V+1) for _ in range(V+1)]
G = [[] for _ in range(V+1)]
print(G)
for _ in range(E):
    u, v = map(int, input().split())
    print(u, v, end=' ')
    # G[u][v] = G[v][u] = 1
    # G[u].append(v)
    # G[v].append(u)

# for i in range(1, V+1):
#     print(i, '-->', G[i])
# for lst in G[1:]:
#     print(*lst[1:])

visited = [0] * (V+1)

# 재귀
# 모든 정점을 다도는데, 이 정점이 인접 정점이면서, 방문하지 않았다면 나를 또 부른다.

# def dfs(v):             # v: 현재 방문하는 정점
#     visited[v] = 1
#     print(v, end=' ')
#     # 방문하지 않은 인접정점을 찾는다.
#     for w in range(1, V+1):
#         if G[v][w] == 1 and not visited[w]:
#             dfs(w)
#
# dfs(1) # v가 처음 시작하는 곳