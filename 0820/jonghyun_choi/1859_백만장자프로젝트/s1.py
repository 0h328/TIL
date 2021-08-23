import sys
sys.stdin = open('input.txt')

T = int(input())

for case in range(T):
    N = int(input())
    data_list = list(map(int,input().split()))
    data_list = data_list[::-1]
    max_val = data_list[0]
    res = 0
    for data in data_list:
        if max_val > data:
            res += (max_val - data)
        else:
            max_val = data
    print('#{} {}'.format(case + 1, res))