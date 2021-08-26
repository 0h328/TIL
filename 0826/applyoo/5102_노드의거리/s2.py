import sys
sys.stdin = open('input.txt')


def dfs(depth, n):
    global result
    if n == G:
        result = min(result, depth) if result != 0 else depth
        return

    visited.add(n)

    for i in node[n]:
        if i not in visited:
            dfs(depth+1, i)


T = int(input())
for test in range(T):
    V, E = map(int, input().split())
    node = [[] for _ in range(V+1)]
    visited = set()
    result = 0

    for _ in range(E):
        a, b = map(int, input().split())
        node[a].append(b)
        node[b].append(a)

    S, G = map(int, input().split())
    dfs(0, S)
    print('#{} {}'.format(test+1, result))
