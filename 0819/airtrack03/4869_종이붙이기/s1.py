import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    ans = [0 for _ in range(N//10 + 1)]

    ans[0] = 1
    ans[1] = 1
    # 점화식: i-1에서 10 늘어나는 경우가 1가지, i-2에서 20 늘어나는 경우가 20을 세로로 자르는 경우 제외하고 2가지
    for i in range(2, N//10 + 1):
        ans[i] = ans[i-1] + ans[i-2] * 2

    print('#{} {}'.format(tc, ans[N//10]))
