import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = tuple(map(int, input().split()))

    max_val = 0
    min_val = 10000 * N     # 최소값 설정: a의 최대값 * 숫자 개수

    for i in range(N-M+1):
        sum_val = 0

        for j in range(M):
            sum_val += data[i+j]

        if max_val < sum_val:
            max_val = sum_val
        if min_val > sum_val:
            min_val = sum_val

    ans = max_val - min_val
    print('#{} {}'.format(tc, ans))