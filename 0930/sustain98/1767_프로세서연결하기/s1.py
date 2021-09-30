import sys
sys.stdin = open('input.txt')

## 테케 하나를 통과 못함
## 아마 전체 코어가 다 연결되지 않을수도 있는 경우에 대해 고려 못했기 때문인듯
def dfs(i, s):
    global res
    if i == len(cores):
        if len(s) < res:
            res = len(s)
    else:
        for j in range(4):
            new_s, tf = check_dir(cores[i][0], cores[i][1], j, s)
            if tf:
                dfs(i+1, s | new_s)


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
    res = n*n
    for i in range(n):
        sub = list(map(int, input().split()))
        for j in range(n):
            if sub[j]:
                cores.append((i, j))

    dfs(0, set(cores))
    res -= len(cores)
    print('#{} {}'.format(idx, res))