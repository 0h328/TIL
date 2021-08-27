import sys
sys.stdin = open('input.txt')


def bfs(start):
    bfs_list = deque([start])
    visited.add(start)
    DP[start] = 0

    while bfs_list:
        n = bfs_list.popleft()

        if n == G:
            return DP[G]

        for i in node[n]:
            if i not in visited:
                bfs_list.append(i)
                visited.add(i)
                DP[i] = DP[n] + 1
    return 0


from collections import deque

T = int(input())
for test in range(T):
    V, E = map(int, input().split())
    node = [[] for _ in range(V+1)]
    visited = set()
    DP = [0] * (V+1)

    for _ in range(E):
        a, b = map(int, input().split())
        node[a].append(b)
        node[b].append(a)

    S, G = map(int, input().split())
    print('#{} {}'.format(test+1, bfs(S)))
