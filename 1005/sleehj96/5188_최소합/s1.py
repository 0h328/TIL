import sys
sys.stdin = open('input.txt')

dr = (0, 1)
dc = (1, 0)


def go(v, my_sum):      # 좌표, 누적합
    global ans

    if v == (N-1, N-1):
        if ans > my_sum:
            ans = my_sum
        return

    for d in range(2):
        n_row = v[0] + dr[d]
        n_col = v[1] + dc[d]

        if 0 <= n_row < N and 0 <= n_col < N:
            go((n_row, n_col), my_sum + G[n_row][n_col])


for tc in range(int(input())):
    N = int(input())
    G = [list(map(int, input().split())) for _ in range(N)]

    ans = 987654321
    go((0, 0), G[0][0])

    print('#{0} {1}'.format(tc+1, ans))
    # break
