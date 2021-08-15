import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

nums_match = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

T = int(input())

for t in range(1, T+1):
    input()
    str_nums = list(input().split())
    nums_list = [0] * 10

    for str_num in str_nums:
        nums_list[nums_match.index(str_num)] += 1

    print('#{}'.format(t))
    for idx, str_num in enumerate(nums_match):
        for _ in range(nums_list[idx]):
            print(str_num, end=' ')
    print()
