import sys

sys.stdin = open('input.txt')

T = int(input())

def calc_perm(n, k, total):
    global ans
    if total >= ans:
        return

    if n == k:
        if total < ans:
            ans = total
        return

    for i in range(N):
        if not chk[i]:
            total += factory[k][i]
            chk[i] = 1
            calc_perm(n, k+1, total)
            total -= factory[k][i]
            chk[i] = 0


for tc in range(1, T + 1):
    N = int(input())
    factory = [list(map(int, input().split())) for _ in range(N)]
    chk = [0] * N

    ans = 99 * N

    calc_perm(N, 0, 0)

    print('#{} {}'.format(tc, ans))