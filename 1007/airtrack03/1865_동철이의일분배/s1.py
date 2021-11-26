import sys

sys.stdin = open('input.txt')

T = int(input())

def perm(n, k, total):
    global ans
    if total <= ans:    # 곱할수록 total 작아지므로
        return

    if k == n:
        if total > ans:
            ans = round(total, 8)
        return

    for i in range(N):
        if not visited[i]:
            cur_percent = data[k][i]
            visited[i] = 1
            perm(n, k+1, total*cur_percent*(10**-2))
            visited[i] = 0


for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    ans = 0

    visited = [0] * N
    perm(N, 0, 1)

    ans = str(ans).split('.')[1]
    ans = ans.ljust(8, '0')
    int_part = ans[:2].lstrip('0')
    float_part = ans[2:]
    ans = int_part + '.' + float_part

    print('#{} {}'.format(tc, ans))