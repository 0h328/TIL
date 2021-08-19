import sys
sys.stdin = open('input.txt')


def dfs(node):
    global result
    if node == G:
        result = 1
        return
    visited[node] = True

    for next_node in node_map[node]:
        if not visited[next_node]:
            dfs(next_node)


T = int(input())
for test in range(T):
    V, E = map(int, input().split())

    result = 0
    visited = [False] * (V+1)
    node_map = [[] for _ in range(V+1)]
    for _ in range(E):
        x, y = map(int, input().split())
        node_map[x].append(y)
    S, G = map(int, input().split())
    dfs(S)
    print('#{} {}'.format(test+1, result))
