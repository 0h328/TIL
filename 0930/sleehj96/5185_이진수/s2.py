import sys
sys.stdin = open('input.txt')


def int_to_decimal(n):
    t_ans = ''
    while n > 0:
        t_ans += str(n % 2)
        n //= 2
    return t_ans[::-1].zfill(4)


for tc in range(int(input())):
    N, hex_num = input().split()

    ans = ''
    for i in range(int(N)):
        # t_num = int(hex_num[i], 16)
        # print(bin(t_num))
        ans += bin(hex_num[i])[2:]

    # ans = 0
    print('#{} {}'.format(tc+1, ans))
    # break
