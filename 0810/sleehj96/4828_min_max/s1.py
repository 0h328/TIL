import sys

sys.stdin = open('input.txt')

t = int(input())

i = 1
while i <= t:
    n = int(input())
    num_list = list(map(int, input().split()))

    my_max = my_min = num_list[0]

    for num in num_list:
        if my_max < num:
            my_max = num
        if my_min > num:
            my_min = num

    print('#{0} {1}'.format(i, my_max-my_min))
    i += 1
