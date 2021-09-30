import sys
sys.stdin = open('input.txt')


def hex_to_bin(hex):
    bin = ''
    for i in range(len(hex)):
        temp_b = ''

        if 47 < ord(hex[i]) < 58:
            temp_h = ord(hex[i]) - 48
        elif ord(hex[i]) > 64:
            temp_h = ord(hex[i]) - 55

        while temp_h:
            temp_b += str(temp_h % 2)
            temp_h //= 2

        while len(temp_b) != 4: # 4자리수로 맞춰 주기
            temp_b += '0'

        bin += temp_b[::-1] # 거꾸로 돌려서 넣어줌
    return bin

T = int(input())
for t in range(1, T+1):
    N, hex = map(str, input().split())
    print('#{} {}'.format(t, hex_to_bin(hex)))