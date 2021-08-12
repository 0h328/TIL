import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split()) # N원소 갯수, K합
    arr = [i for i in range(1, 13)]
    len_arr = len(arr)
    result = 0
    for i in range(1<<len_arr):
        cnt = 0
        sum_list = 0
        for j in range(len_arr):
            if i & (1 << j):
                cnt += 1
                sum_list += arr[j]
        if cnt == N and sum_list == K:
            result += 1
    print('#{} {}'.format(test_case, result))