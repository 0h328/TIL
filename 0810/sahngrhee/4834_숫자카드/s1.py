import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    my_list = list(map(int, input()))

    c = [0] * 10
    for i in range(N):
        c[my_list[i]] += 1

    my_max = c[0]
    my_num = 0
    for i in range(len(c)):
        if my_max <= c[i]:
            my_max = c[i]
            my_num = i
    print('#{} {} {}'.format(test_case, my_num, my_max))