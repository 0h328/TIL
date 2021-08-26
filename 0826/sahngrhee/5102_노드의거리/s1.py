def bfs(v):
    global ans
    queue = []
    queue.append(v)
    visited[v] = 1
    while queue:
        tmp = queue.pop(0)
        for i in adj_list[tmp]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[tmp] + 1
    return visited[G]

import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        adj_list[a].append(b)
        adj_list[b].append(a)
    S, G = map(int, input().split())
    visited = [0 for _ in range(V + 1)]

    if bfs(S):
        ans = bfs(S) - 1
    else:
        ans = 0

    print('#{} {}'.format(test_case, ans))