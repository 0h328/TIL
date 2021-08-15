import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(1, T+1):
    tc, length = list(input().split())
    str_list = list(input().split())
    new_list = []
    order = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    for i in range(10):
        for strs in str_list:
            if strs == order[i]:
                new_list.append(strs)
    print(tc)
    for a in new_list:
        print(a, end=' ')
    print()
