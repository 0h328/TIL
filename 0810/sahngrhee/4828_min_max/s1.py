import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    my_list = list(map(int, input().split()))

    my_min = my_list[0]
    my_max = my_list[0]

    for i in range(N):
        if my_list[i] > my_max:
            my_max = my_list[i]

    for i in range(N):
        if my_list[i] < my_min:
            my_min = my_list[i]

    ans = my_max - my_min
    print('#{} {}'.format(test_case, ans))