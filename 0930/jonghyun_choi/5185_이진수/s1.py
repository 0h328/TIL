import sys
sys.stdin = open('input.txt')

T = int(input())

hex_data = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111',
}


for case in range(T):
    N, M = input().split()
    res = ''
    for i in M:
        res += hex_data[i]
    print('#{} {}'.format(case + 1, res))
