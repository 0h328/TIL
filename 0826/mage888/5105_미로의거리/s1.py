import sys
sys.stdin = open('input.txt')

def dfs(start_r, start_c):

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]

    cnt = 0

    for r in range(N):
        for c in range(N):
            if data[r][c] == 2:
                break

    ans = dfs(r, c)

    # print('#{} {}'.format(tc, ans))