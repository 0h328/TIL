import sys

sys.stdin = open('input.txt')

T = int(input())
idx = 1

while idx <= T:
    N = int(input())
    input_num_list = list(map(int, input().split()))

    ans_list = []

    i = 0
    while i < 5:

        max_idx = input_num_list.index(max(input_num_list))
        ans_list.append(input_num_list.pop(max_idx))
        min_idx = input_num_list.index(min(input_num_list))
        ans_list.append(input_num_list.pop(min_idx))

        i += 1


    ans = ' '.join(map(str, ans_list))

    print('#{0} {1}'.format(idx, ans))

    idx += 1
