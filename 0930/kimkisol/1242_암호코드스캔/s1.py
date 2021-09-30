import sys

sys.stdin = open('input.txt')
'''
 “(홀수 자리의 합 x 3) + 짝수 자리의 합 + 검증 코드” 가 10의 배수가 되어야 한다.
'''

asc = [[0, 0, 0, 0],  # 0
       [0, 0, 0, 1],  # 1
       [0, 0, 1, 0],  # 2
       [0, 0, 1, 1],  # 3
       [0, 1, 0, 0],  # 4
       [0, 1, 0, 1],  # 5
       [0, 1, 1, 0],  # 6
       [0, 1, 1, 1],  # 7
       [1, 0, 0, 0],  # 8
       [1, 0, 0, 1],  # 9
       [1, 0, 1, 0],  # A
       [1, 0, 1, 1],  # B
       [1, 1, 0, 0],  # C
       [1, 1, 0, 1],  # D
       [1, 1, 1, 0],  # E
       [1, 1, 1, 1]]  # F


def ascii_to_hex(c):
    # 9 이하
    if c <= '9':
        return ord(c) - ord('0')
    # 10 이상
    else:
        return ord(c) - ord('A') + 10


def hex_to_binary(x):
    for i in range(4):
        bin_list.append(asc[x][i])


def Verify(code, n):  # 1개 배열 / n: 길이 배수
    check = 0
    result = 0
    for i in range(8):
        # print(i, n, 7*i*n, (7*i+7)*n, len(code), code)
        # print(code[7*i*n:7*i+(7*n):n])
        num = secret_code.index(code[7*i*n:(7*i+7)*n:n])
        if i % 2 == 0:
            check += num * 3
        else:
            check += num
        result += num

    if check % 10 == 0:
        return result
    return 0

for i in range(len(asc)):
    print(*asc[i], end=', ')

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())  # N: 행, M : 열
    input_code = [list(input()) for _ in range(N)]
    secret_code = [
        [0, 0, 0, 1, 1, 0, 1],  # 0
        [0, 0, 1, 1, 0, 0, 1],  # 1
        [0, 0, 1, 0, 0, 1, 1],  # 2
        [0, 1, 1, 1, 1, 0, 1],  # 3
        [0, 1, 0, 0, 0, 1, 1],  # 4
        [0, 1, 1, 0, 0, 0, 1],  # 5
        [0, 1, 0, 1, 1, 1, 1],  # 6
        [0, 1, 1, 1, 0, 1, 1],  # 7
        [0, 1, 1, 0, 1, 1, 1],  # 8
        [0, 0, 0, 1, 0, 1, 1],  # 9
    ]
    codes = []
    res = 0

    for i in range(N):
        j = 0
        while j < M:
            if input_code[i][j] != '0':
                if input_code[i][j] == input_code[i-1][j]:
                    break
                k = 0
                while j+(k*15) < M and input_code[i][j+(k*15)] != '0':
                    k += 1
                codes.append(input_code[i][j:j+(k*15)])
                j += k*15
            else:
                j += 1

    for code in codes:
        bin_list = []

        for i in range(len(code)):
            hex_to_binary(ascii_to_hex(code[i]))

        while bin_list[-1] == 0:
            bin_list.insert(0, bin_list.pop())

        if bin_list[0] == 0:
            for _ in range(len(bin_list) % 56):
                bin_list.pop(0)
        else:
            for _ in range(56 - len(bin_list) % 56):
                bin_list.insert(0, 0)

        print(len(bin_list), len(bin_list) // 56, bin_list)
        res += Verify(bin_list, len(bin_list) // 56)

    print('#{} {}'.format(t, res))
