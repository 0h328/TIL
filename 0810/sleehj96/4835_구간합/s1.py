import sys

sys.stdin = open('input.txt')

t = int(input())

i = 1
while i <= t:
    n, m = map(int, input().split())
    num_list = list(map(int, input().split()))

    my_max = my_min = sum(num_list[:m])

    for idx in range(len(num_list) - m + 1):
        temp_sum = sum(num_list[idx:idx + m])
        if temp_sum > my_max:
            my_max = temp_sum
        if temp_sum < my_min:
            my_min = temp_sum

    print('#{0} {1}'.format(i, my_max-my_min))
    i += 1
