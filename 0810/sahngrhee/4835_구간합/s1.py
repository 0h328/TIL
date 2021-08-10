import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    my_list = list(map(int, input().split()))

    my_sum_list = []
    for i in range(0, N-M+1):
        my_sum = 0
        for j in range(i, i+M):
            my_sum += my_list[j]
        my_sum_list.append(my_sum)

    my_min = my_sum_list[0]
    my_max = my_sum_list[0]

    for i in range(len(my_sum_list)):
        if my_sum_list[i] > my_max:
            my_max = my_sum_list[i]

    for i in range(len(my_sum_list)):
        if my_sum_list[i] < my_min:
            my_min = my_sum_list[i]

    ans = my_max - my_min
    print('#{} {}'.format(test_case, ans))