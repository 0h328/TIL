import sys
sys.stdin = open('input.txt')

def dfs(g):
    loc, dest = 0, 99
    visited = [0] * 100
    visited[loc] = 1
    stack = []

    while loc != dest:
        for i in g[loc]:
            if visited[i] == 0:
                stack.append(i)
                visited[i] = 1
                loc = i
                break
        else:
            if not stack:
                return 0
            else:
                loc = stack.pop()
    return 1

for idx in range(1,11):
    t, num = map(int, input().split())
    road = list(map(int, input().split()))
    g = [[] for _ in range(100)]
    for i in range(0, 2*num, 2):
        g[road[i]].append(road[i+1])

    print('#{} {}'.format(idx, dfs(g)))