import sys
sys.stdin = open('input.txt')

T = int(input())

def ascii_to_hex(c):
    if '0' <= c <= '9':
        return ord(c) - ord('0')
    return ord(c) - ord('A') + 10

def hex_to_binary(hex_num):
    result = ''
    for i in range(3, -1, -1):
        if hex_num & (1 << i):
            result += '1'
        else:
            result += '0'
    return result

for tc in range(1, T+1):
    N, hex_data = input().split()
    N = int(N)

    ans = ''

    for i in range(N):
        ans += hex_to_binary(ascii_to_hex(hex_data[i]))

    print('#{} {}'.format(tc, ans))