import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    my_sum_list = []

    for i in range(100):
        my_sum = 0
        for j in range(100):
            my_sum += arr[i][j]
        my_sum_list.append(my_sum)

    for j in range(100):
        my_sum = 0
        for i in range(100):
            my_sum += arr[i][j]
        my_sum_list.append(my_sum)

    my_sum = 0
    for i in range(100):
        for j in range(100):
            if i == j:
                my_sum += arr[i][j]
    my_sum_list.append(my_sum)

    my_sum = 0
    for i in range(100):
        my_sum += arr[i][99-i]
    my_sum_list.append(my_sum)

    ans = max(my_sum_list)
    print('#{} {}'.format(test_case, ans))