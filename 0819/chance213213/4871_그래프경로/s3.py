import sys
# import pprint
sys.stdin = open('input.txt')

def dfs(start, end):
    visited[start] = 1
    for w in G[start]:
        if not visited[w]:
            dfs(w, end)
    return visited[end]

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    #방향성 그래프래,,,
    for _ in range(E):
        s, e = map(int, input().split())
        G[s].append(e)
    start, goal = map(int, input().split())
    # print(G)
    # pprint.pprint(G)
    ans = dfs(start, goal)
    print('#{} {}'.format(tc, ans))
    print(visited)

