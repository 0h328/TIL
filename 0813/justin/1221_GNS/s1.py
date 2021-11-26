code = [[[0 for _ in range(128)] for _ in range(128)]for _ in range(128)]
code[ord('Z')][ord('R')][ord('O')] = 0
code[ord('O')][ord('N')][ord('E')] = 1
code[ord('T')][ord('W')][ord('O')] = 2
code[ord('T')][ord('H')][ord('R')] = 3
code[ord('F')][ord('O')][ord('R')] = 4
code[ord('F')][ord('I')][ord('V')] = 5
code[ord('S')][ord('I')][ord('X')] = 6
code[ord('S')][ord('V')][ord('N')] = 7
code[ord('E')][ord('G')][ord('T')] = 8
code[ord('N')][ord('I')][ord('N')] = 9

digit = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    temp = input()
    data = list(map(str, input().split()))
    count = [0 for _ in range(10)]
    for i in range(len(data)):
        count[code[ord(data[i][0])][ord(data[i][1])][ord(data[i][2])]] += 1

    print('#{}'.format(tc), end=' ')
    for i in range(10):
        for _ in range(count[i]):
            print(digit[i], end=' ')
    print()
