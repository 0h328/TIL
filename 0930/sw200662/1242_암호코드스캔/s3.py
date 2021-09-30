import sys

sys.stdin = open('input.txt')

T = int(input())

find_password_list = [['0001101'], ['0011001'], ['0010011'], ['0111101'], ['0100011'], ['0110001'], ['0101111'],
                      ['0111011'], ['0110111'], ['0001011']]

binary_nums = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}


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
    new = []
    for _ in range(N):
        row = input().rstrip()
        temp = ''
        for i in range(M):
            temp += binary_nums[row[i]]
        new.append(temp)
    new = list(set(new))


    for i in find_list3:
        z = len(i) // 56

        for b in range(len(i) - 1, -1, -1):
            if i[b] == str(1):
                end = b
                i = i[end - (56 * z) + 1:end + 1]
                break
        if z != 1:
            temp_num = ''
            for q in range(len(i)):
                if q % z == 0:
                    temp_num += i[q]
            i = temp_num
        check = 0
        ans = 0

        for b in range(1, 9):
            temp_list = i[b * 7 - 7:b * 7]
            for c in range(len(find_password_list)):
                if find_password_list[c] == [temp_list]:
                    if b % 2 == 1:
                        check += c * 3
                        ans += c
                    else:
                        check += c
                        ans += c
        if check % 10 == 0:
            real_ans += ans
        else:
            pass