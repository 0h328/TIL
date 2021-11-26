def sovle(data):
    # 숫자 -> 외계어
    def get_human_num(s):
        if s == 'ZRO':
            return 0
        elif s == 'ONE':
            return 1
        elif s == 'TWO':
            return 2
        elif s == 'THR':
            return 3
        elif s == 'FOR':
            return 4
        elif s == 'FIV':
            return 5
        elif s == 'SIX':
            return 6
        elif s == 'SVN':
            return 7
        elif s == 'EGT':
            return 8
        elif s == 'NIN':
            return 9

    # 외계어 -> 숫자
    def get_alien_num(n):
        if n == 0:
            return 'ZRO'
        elif n == 1:
            return 'ONE'
        elif n == 2:
            return 'TWO'
        elif n == 3:
            return 'THR'
        elif n == 4:
            return 'FOR'
        elif n == 5:
            return 'FIV'
        elif n == 6:
            return 'SIX'
        elif n == 7:
            return 'SVN'
        elif n == 8:
            return 'EGT'
        elif n == 9:
            return 'NIN'

    numbers = sorted(map(get_human_num, data))
    result = ' '.join(map(get_alien_num, numbers))
    return result


import sys

sys.stdin = open('input.txt')
T = int(input())
for _ in range(1, T + 1):
    tc, N = input().split()
    data = input().split()
    ans = sovle(ans)
    print('{}\n{}'.format(tc, ans))