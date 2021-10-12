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
    temp = [list(map(int, input().split())) for _ in range(E)]
    # print(temp)
    # temp = sum(temp, [])
    # pprint.pprint(temp)
    st, en = map(int, input().split())
    G = [[] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    # print(visited)
    # print(st, en)
    for i in range(E):
        G[temp[i][0]].append(temp[i][1])
        # G[temp[i][1]].append(temp[i][0])
    # print(G)
    ans = dfs(st, en)
    print('#{} {}'.format(tc, ans))
    # print(visited)

