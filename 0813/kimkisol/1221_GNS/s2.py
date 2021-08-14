import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

nums_match = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

T = int(input())

for t in range(1, T+1):
    test_case, N = input().split()
    str_nums = list(input().split())

    new_str_nums = sorted(str_nums, key=lambda x: nums_match[x])

    print(test_case)
    for str_num in new_str_nums:
        print(str_num, end=' ')
    print()
