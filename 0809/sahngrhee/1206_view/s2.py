import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    N = int(input())
    my_list = list(map(int, input().split()))
    total = 0
    idx_list = [-2, -1, 1, 2]
    for i in range(2, N-2):
        second_max = my_list[i-2]
        if (my_list[i] > my_list[i-1]) and (my_list[i] > my_list[i-2]) and (my_list[i] > my_list[i+1]) and (my_list[i] > my_list[i+2]):
            for idx in idx_list:
                if second_max < my_list[i+idx]:
                    second_max = my_list[i+idx]
            total += my_list[i] - second_max
    print('#{} {}'.format(test_case, total))
