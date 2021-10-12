import sys
# 146ms
sys.stdin = open('input.txt')


def find_num(b_num):
    for j in range(len_t):  # 3진수 앞~뒤까지
        for k in range(3):  # 0, 1, 2
            if k != t_lst[j]:  # 기존 수가 아니면
                t_num = t_ten + 3 ** (len_t - j - 1) * (k - t_lst[j])  # k: 새로 바뀐 수, t_lst[j]: 기존 수
                if t_num == b_num:
                    return True


T = int(input())

for tc in range(1, T + 1):
    b = input()
    b_ten = int('0b' + b, 2)
    len_b = len(b)

    t = input()
    t_ten = int(t, 3)
    t_lst = list(map(int, list(t)))  # 3진수
    len_t = len(t)

    for i in range(len_b):
        b_num = b_ten + 2 ** (len_b - i - 1) if b[i] == '0' else b_ten - 2 ** (len_b - i - 1)  # 0이면 더하고 1이면 빼고. len_b - i - 1은 자릿수 개념
        if find_num(b_num):
            break

    print('#{} {}'.format(tc, b_num))
