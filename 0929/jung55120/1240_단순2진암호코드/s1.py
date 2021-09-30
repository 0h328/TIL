import sys
sys.stdin = open('input.txt')

amho = {  # 딕셔너리
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # 배열의 세로, 가로 길이
    code = [list(map(int, input())) for _ in range(N)]
    # print(code)
    ans = []
    for i in range(N):
        for j in range(M-1, -1, -1):
            if code[i][j] == 1:
                ans = code[i][j-55:j+1]
                break
    amho_list = []
    for j in range(0, 8):
        amho_str = ''
        for k in range(0, 7):
            amho_str += str(ans[7*j+k])
        amho_list.append(amho_str)
    number = ''
    for l in amho_list:
        if l in amho:
            number += str(amho[l])
        else:
            print('#{} {}'.format(tc, 0))
    number = list(map(int, number))
    sum_num = 0
    for i in range(len(number)):
        if i % 2 == 0:
            sum_num += number[i] * 3
        else:
            sum_num += number[i]
    result = sum_num % 10
    cnt = 0
    if result != 0:
        print('#{} {}'.format(tc, 0))
    else:
        for m in number:
            cnt += m
        print('#{} {}'.format(tc, cnt))