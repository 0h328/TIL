import sys
sys.stdin = open('input.txt')

def dfs(i, s, connected_core):
    global res, max_connected
    if i == len(cores):
        if max_connected < connected_core:
            max_connected = connected_core
            res = len(s)
        elif max_connected == connected_core and len(s) < res:
            res = len(s)
    elif len(s) <= res:
        for j in range(4):
            new_s, tf = check_dir(cores[i][0], cores[i][1], j, s)
            if tf:
                dfs(i+1, s | new_s, connected_core + 1)
        dfs(i+1, s, connected_core)


def check_dir(x, y, dir, s):
    new_s = set()
    x += dx[dir]
    y += dy[dir]
    while -1 < x < n and -1 < y < n:
        if (x, y) in s:
            return (set(), 0)
        else:
            new_s.add((x, y))
        x += dx[dir]
        y += dy[dir]
    return (new_s, 1)


t = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for idx in range(1, t+1):
    n = int(input())
    l = []
    cores = []
    res = n * n
    max_connected = 0
    for i in range(n):
        sub = list(map(int, input().split()))
        for j in range(n):
            if sub[j]:
                cores.append((i, j))

    dfs(0, set(cores), 0)

    res -= len(cores)

    print('#{} {}'.format(idx, res))

