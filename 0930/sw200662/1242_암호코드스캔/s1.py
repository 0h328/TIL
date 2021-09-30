import sys

sys.stdin = open('input.txt')

T = int(input())

find_password_list = [['0001101'], ['0011001'], ['0010011'], ['0111101'], ['0100011'], ['0110001'], ['0101111'],
                      ['0111011'], ['0110111'], ['0001011']]

asc = [[0, 0, 0, 0],  # 2진법 - 0(16진법)
       [0, 0, 0, 1],  # 2진법 - 1(16진법)
       [0, 0, 1, 0],  # 2진법 - 2(16진법)
       [0, 0, 1, 1],  # 2진법 - 3(16진법)
       [0, 1, 0, 0],  # 2진법 - 4(16진법)
       [0, 1, 0, 1],  # 2진법 - 5(16진법)
       [0, 1, 1, 0],  # 2진법 - 6(16진법)
       [0, 1, 1, 1],  # 2진법 - 7(16진법)
       [1, 0, 0, 0],  # 2진법 - 8(16진법)
       [1, 0, 0, 1],  # 2진법 - 9(16진법)
       [1, 0, 1, 0],  # 2진법 - A(16진법) - 10
       [1, 0, 1, 1],  # 2진법 - B(16진법) - 11
       [1, 1, 0, 0],  # 2진법 - C(16진법) - 12
       [1, 1, 0, 1],  # 2진법 - D(16진법) - 13
       [1, 1, 1, 0],  # 2진법 - E(16진법) - 14
       [1, 1, 1, 1]]  # 2진법 - F(16진법) - 15


def ascii_to_hex(c):
    # 9이하인 경우 16진수 변환
    if c <= '9':
        return ord(c) - ord('0')
    # 10이상인 경우 16진수 변환
    else:
        return ord(c) - ord('A') + 10


def hex_to_binary(x):
    for i in range(4):
        t.append(asc[x][i])


for tc in range(T):
    N, M = map(int, input().split())
    input_list = [input() for _ in range(N)]
    find_list = []
    find_list2 = []
    start = 0
    end = 0
    for k in input_list:
        for i in range(len(k)):
            if k[i] != str(0):
                start = i
                find_list = k
                break
        for i in range(len(k) - 1, -1, -1):
            if k[i] != str(0):
                end = i
                break
        if start != 0 and end != 0:
            find_list2.append(find_list[start:end + 1])
    find_list2 = list(set(find_list2))
    t = []
    num_str = '0000'
    for c in find_list:
        hex_to_binary(ascii_to_hex(c))
    for d in t:
        num_str += str(d)

    z = len(num_str) // 56

    for i in range(len(num_str) - 1, -1, -1):
        if num_str[i] == str(1):
            end = i
            num_str = num_str[end - (56 * z) + 1:end + 1]
            break


    if z != 1:
        temp_num = ''
        for q in range(len(num_str)):
            if q % z == 0:
                temp_num += num_str[q]
        num_str = temp_num

    check = 0
    ans = 0

    for b in range(1, 9):
        temp_list = num_str[b * 7 - 7:b * 7]
        for c in range(len(find_password_list)):
            if find_password_list[c] == [temp_list]:
                if b % 2 == 1:
                    check += c * 3
                    ans += c
                else:
                    check += c
                    ans += c
    if check % 10 == 0:
        print('#{} {}'.format(tc + 1, ans))
    else:
        print('#{} {}'.format(tc + 1, 0))
