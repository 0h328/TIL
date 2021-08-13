# .replace 활용

import sys
sys.stdin = open('input.txt')

num_list = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

T = int(input())

for tc in range(1, T+1):
    N = int(input().split()[1])
    data = input()

    for num, num_str in enumerate(num_list):
        data = data.replace(num_str, str(num))

    data_list = data.split()
    data_list.sort()
    ans = ' '.join(data_list)

    for num, num_str in enumerate(num_list):
        ans = ans.replace(str(num), num_str)

    print('#{}'.format(tc))
    print(ans)