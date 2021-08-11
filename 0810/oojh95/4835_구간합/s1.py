import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    number = list(map(int, input().split()))

    min_sum = 1000000
    max_sum = 0
    for i in range(N-M+1):
        sum_part = 0
        for j in range(M):
            sum_part += number[i+j]
        if sum_part > max_sum:
            max_sum = sum_part
        if sum_part < min_sum:
            min_sum = sum_part
    result = max_sum - min_sum

    print('#{} {}'.format(test_case, result))
