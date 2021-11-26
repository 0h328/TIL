import sys

sys.stdin = open('input.txt')


asc = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']

def ascii_to_hex(c):
    # 9 이하
    if c <= '9':
        return ord(c) - ord('0')
    # 10 이상
    else:
        return ord(c) - ord('A') + 10

T = int(input())

for t in range(1, T + 1):
    N, hex_nums = input().split()
    bin_nums = ''

    for hex_num in list(hex_nums):
        bin_nums += asc[ascii_to_hex(hex_num)]

    print('#{} {}'.format(t, bin_nums))