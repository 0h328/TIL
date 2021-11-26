import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    num_list = input()

    cnt = [0] * 10

    for num in num_list:
        cnt[int(num) % 10] += 1

    max_cnt = cnt[0]
    max_num = 0
    for i in range(1, 10):
        if cnt[i] >= max_cnt:
            max_cnt = cnt[i]
            max_num = i
    print('#{} {} {}'.format(test_case, max_num, max_cnt))

