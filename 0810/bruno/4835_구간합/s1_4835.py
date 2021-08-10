import sys
sys.stdin = open('input.txt')

T = int(input())

def sum_sec(N, M, arr):
    max_sum = 0
    min_sum = 10000 * M

    for i in range(0, N-M+1):
        summ = 0
        for j in range(M):
            summ += arr[i+j]

        if summ > max_sum:
            max_sum = summ
        if summ < min_sum:
            min_sum = summ

    return max_sum - min_sum

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = sum_sec(N, M, arr)
    print('#{} {}'.format(tc, ans))
