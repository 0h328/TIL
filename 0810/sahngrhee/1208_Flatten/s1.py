import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    N = int(input())
    my_list = list(map(int, input().split()))
    count = [0] * 101

    my_min = 100
    my_max = 1

    for i in range(100):
        count[my_list[i]] += 1
        if my_list[i] > my_max:
            my_max = my_list[i]
        if my_list[i] < my_min:
            my_min = my_list[i]

    while N > 0:
        count[my_min] -= 1
        count[my_min+1] += 1
        count[my_max] -= 1
        count[my_max-1] += 1
        if count[my_min] == 0:
            my_min += 1
        if count[my_max] == 0:
            my_max -= 1
        N -= 1

    ans = my_max - my_min
    print('#{} {}'.format(test_case, ans))




