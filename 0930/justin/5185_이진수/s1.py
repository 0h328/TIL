# hex -> bin
asc = [[0, 0, 0, 0],   #0
       [0, 0, 0, 1],   #1
       [0, 0, 1, 0],   #2
       [0, 0, 1, 1],   #3
       [0, 1, 0, 0],   #4
       [0, 1, 0, 1],   #5
       [0, 1, 1, 0],   #6
       [0, 1, 1, 1],   #7
       [1, 0, 0, 0],   #8
       [1, 0, 0, 1],   #9
       [1, 0, 1, 0],   #A
       [1, 0, 1, 1],   #B
       [1, 1, 0, 0],   #C
       [1, 1, 0, 1],   #D
       [1, 1, 1, 0],   #E
       [1, 1, 1, 1]]   #F

# ASCII -> 16
def ascii_to_hex(c):
    if c <= '9':                        # 9 이하면
        return ord(c) - ord('0')        # 48
    else:                               # 10 이상이면
        return ord(c) - ord('A') + 10   # 65

# 16 -> 2
def hex_to_bin(x):
    for i in range(4):             # 4bit 내부를 돌며
        bin_list.append(asc[x][i]) # 2진수로 변환된 값을 담자

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    bin_list = []                        # 변환된 2진수를 담을 리스트
    N, arr = input().split()             # 자리수 N, N자리 16진수
    for i in range(int(N)):              # 16진수 변환 -> 2진수 변환
        hex_to_bin(ascii_to_hex(arr[i]))
    print('#{}'.format(tc), end=' ')

    for i in range(len(bin_list)):
        print(bin_list[i], end='')
    print()