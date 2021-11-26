import sys
sys.stdin = open('input.txt')


def dfs(r, c, cnt):
    global tmp, set_result
    if cnt == 7:
        set_result.add(tmp)
        return
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < 4 and 0 <= nc < 4:
            tmp += str(arr[r][c])
            dfs(nr, nc, cnt+1)
            tmp = tmp[:-1]

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    tmp = ''
    set_result = set()
    for k in range(4):
        for j in range(4):
            dfs(k, j, 0)
    print('#{} {}'.format(tc, len(set_result)))