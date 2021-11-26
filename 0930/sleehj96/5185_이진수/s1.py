import sys
sys.stdin = open('input.txt')

hex_string = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
}

def hex_to_int(char):
    # for char in s:
    if char in hex_string:
        return hex_string[char]
    else:
        return int(char)


def int_to_decimal(n):
    t_ans = ''
    while n > 0:
        t_ans += str(n % 2)
        n //= 2
    return t_ans[::-1].zfill(4)     # 1 -> 1, 1->0001


for tc in range(int(input())):
    N, hex_num = input().split()

    ans = ''
    for i in range(int(N)):
        t_num = hex_to_int(hex_num[i])
        ans += int_to_decimal(t_num)

    # ans = 0
    print('#{} {}'.format(tc+1, ans))
    # break
