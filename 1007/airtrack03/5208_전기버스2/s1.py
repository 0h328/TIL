import sys

sys.stdin = open('input.txt')

T = int(input())

def charge(cur, k, n, cnt):
    global ans
    if cnt >= ans:
        return

    cur -= 1

    if k == n or cur >= n - k:
        if ans > cnt:
            ans = cnt
        return

    if cur == 0:    # 무조건 충전해야 하는 경우
        charge(stations[k], k+1, n, cnt+1)
    else:   # 충전 or Pass
        charge(cur, k + 1, n, cnt)  # Pass
        charge(stations[k], k+1, n, cnt+1)  # 충전



for tc in range(1, T + 1):
    data = list(map(int, input().split()))
    N = data[0]
    stations = [0] + data[1:]

    ans = N

    charge(stations[1], 2, N, 0)

    print('#{} {}'.format(tc, ans))