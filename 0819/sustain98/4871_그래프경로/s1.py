import sys
sys.stdin = open('input.txt')


def dfs(g, loc, dest):
    visited = [0] * (v+1)
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


t = int(input())
for num in range(1, t + 1):
    v, e = map(int, input().split())
    g = [[] for _ in range(v + 1)]

    for _ in range(e):
        s, d = map(int, input().split())
        g[s].append(d)
    s, d = map(int, input().split())
    print('#{} {}'.format(num, dfs(g, s, d)))




