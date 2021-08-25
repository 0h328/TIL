import sys
sys.stdin = open('input.txt')

for _ in range(1, 11):
    tc = int(input())
    num_list = list(map(int, input().split()))

    idx = 1
    while num_list[-1] != 0:
        tmp = num_list.pop(0) - idx
        if tmp < 0:
            tmp = 0

        num_list.append(tmp)
        idx += 1

        if idx == 6:
            idx = 1

    print('#{}'.format(tc), end=' ')
    print(*num_list)