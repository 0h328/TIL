import sys
sys.stdin = open('input.txt')

dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]

def dfs(r, c, visit, start_point, cnt, pos):
    global answer
    if pos > 3:
        return

    if (r, c) == start_point and cnt != 0:
        if answer < cnt:
            answer = cnt
        return

    next_r = r + dr[pos]
    next_c = c + dc[pos]
    if 0 <= next_r < N and 0 <= next_c < N and cake[next_r][next_c] not in visit:
        dfs(next_r, next_c, visit + [cake[next_r][next_c]], start_point, cnt + 1, pos)
        dfs(next_r, next_c, visit + [cake[next_r][next_c]], start_point, cnt + 1, pos + 1)


T = int(input())

for case in range(T):
    N = int(input())
    cake = [list(map(int, input().split())) for _ in range(N)]
    answer = -1
    for i in range(N):
        for j in range(N):
            dfs(i, j, [], (i, j), 0, 0)

    print('#{} {}'.format(case + 1, answer))