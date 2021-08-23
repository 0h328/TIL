import sys

sys.stdin = open('input.txt')

T = int(input())

i = 0
while i < T:
    N = int(input())
    my_list = list(map(int, input().split()))
    my_list = my_list[::-1]
    max_num = my_list[0]
    my_sum = 0

    for j in range(1, len(my_list)):
        if max_num > my_list[j]:
            my_sum += max_num - my_list[j]
        else:
            max_num = my_list[j]

    print('#{} {}'.format(i+1, my_sum))
    i += 1