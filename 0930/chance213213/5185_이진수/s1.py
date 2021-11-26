import sys
sys.stdin = open('input.txt')

T = int(input())

def ascii_to_hex(num):
    if num <= '9':
        return ord(num) - ord('0')
    else:
        return ord(num) - ord('A') + 10


def hex_to_binary(num):
    ans = ''
    for j in range(4):
        if num & (1 << j):
            ans = '1' + ans
        else:
            ans = '0' + ans
    return ans


for tc in range(1, T+1):
    N, X = map(str, input().split())
    N = int(N)
    print('#{} '.format(tc), end='')
    for chr in X:
        num = ascii_to_hex(chr)
        print(hex_to_binary(num), end='')
    print()


