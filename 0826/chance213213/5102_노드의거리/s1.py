
def BFS(s, G, n):
    visited = [0] * (n+1)
    queue = []
    queue.append(s)
    visited[s] = 1
    while queue:
        w = queue.pop(0)

        for i in range(1, n+1):
            if full_adj[w][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = visited[w] + 1
                if w == G:
                    queue.clear()

    return visited[G]

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    adj = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    # print(adj)
    full_adj = [[0]*(V+1) for _ in range(V+1)]
    # print(full_adj)
    for num in adj:
        # print(num[0], num[1])
        full_adj[num[0]][num[1]] = 1
        full_adj[num[1]][num[0]] = 1
    # print(full_adj)

    print('#{} {}'.format(tc, BFS(S, G, V)))