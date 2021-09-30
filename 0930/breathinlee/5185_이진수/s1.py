import sys
sys.stdin = open('input.txt')


def dec_to_binary(num):
    res = ''
    for j in range(3, -1, -1):
        if num & 1 << j:
            res += '1'
        else:
            res += '0'
    return res


def hex_to_binary(hex_value):
    dec_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    if hex_value.isdigit():
        dec_value = int(hex_value)
    else:
        dec_value = dec_dict.get(hex_value)

    res = ''
    res += dec_to_binary(dec_value)
    return res


T = int(input())
for tc in range(1, T+1):
    N, lst = input().split()
    binary_num = ''
    for w in lst:
        binary_num += hex_to_binary(w)
    print('#{} {}'.format(tc, binary_num))
