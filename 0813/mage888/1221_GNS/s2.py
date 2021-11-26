import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    no, n = input().split()
    char_n = input().split()

    char_dict = {0: 'ZRO', 1: 'ONE', 2: 'TWO', 3: 'THR', 4: 'FOR', 5: 'FIV', 6: 'SIX', 7: 'SVN', 8: 'EGT', 9: 'NIN'}

    result = ''
    for key, val in char_dict.items():
        result += (val + ' ') * char_n.count(val)

    print('#{}'.format(tc), end=' ')
    print(result)
