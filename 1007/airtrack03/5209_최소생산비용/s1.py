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

def bit_masking(idx, s, visit): # idx:제품 번호, s: 중간 계산 결과, visit: 정수
    global ans
    if idx == N:    # if visit == (1 << N) - 1과 같은 조건문
        if s < ans:
            ans = s
    if s >= ans:
        return
    for j in range(N):  # 공장을 고르자!
        if visit & (1<<j):
            continue
        bit_masking(idx+1, s+factory[idx][j], visit | 1<<j)



for tc in range(1, T + 1):
    N = int(input())
    factory = [list(map(int, input().split())) for _ in range(N)]
    chk = [0] * N

    ans = 99 * N

    calc_perm(N, 0, 0)

    print('#{} {}'.format(tc, ans))