import sys

sys.stdin = open('input.txt')

def dfs(route1, route2):
    stk = []
    visited = [False for _ in range(100)]
    p = route1[0]
    stk.append(p)
    visited[0] = True
    visited[p] = True

    while True:
        if visited[99]:
            return 1

        if route1[p] != -1 and (not visited[route1[p]]):
            stk.append(p)
            p = route1[p]
            visited[p] = True
        elif route2[p] != -1 and (not visited[route2[p]]):
            stk.append(p)
            p = route2[p]
            visited[p] = True
        else:
            if stk:
                p = stk.pop()
            else:
                return 0

    

for tc in range(1, 11):
    tc, n = map(int, input().split())
    nodes = list(map(int, input().split()))
    route1 = [-1] * 100
    route2 = [-1] * 100
    for i in range(0, n*2, 2):
        if route1[nodes[i]] == -1:
            route1[nodes[i]] = nodes[i+1]
        else:
            route2[nodes[i]] = nodes[i+1]

    print('#{} {}'.format(tc, dfs(route1, route2)))
