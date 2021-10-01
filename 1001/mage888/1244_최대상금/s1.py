from itertools import combinations

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    num, s = map(int, input().split())
    num_to_str = str(num)

    length_list = list(range(len(num_to_str)))
    all_case = list(combinations(list(combinations(length_list, 2)),s))

    for i in range(len(all_case)):
        nts_list = list(num_to_str)
        for j in range(len(all_case[i])):
            nts_list[all_case[i][j][0]], nts_list[all_case[i][j][1]] = nts_list[all_case[i][j][1]], nts_list[all_case[i][j][0]]
        max_num = ''.join(nts_list)

        if num < int(max_num):
            num = int(max_num)
    print('#{} {}'.format(tc, num))