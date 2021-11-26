import sys
sys.stdin = open('input.txt')

T = int(input())

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
    t = []
    ans = ''
    words = input().split()
    for k in words[1]:
        hex_to_binary(ascii_to_hex(k))
    for a in t:
        ans += str(a)
    print('#{} {}'.format(tc+1,ans))
