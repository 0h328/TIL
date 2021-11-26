import sys
sys.stdin = open('input.txt')

asc = [[0, 0, 0, 0],  #0
       [0, 0, 0, 1],  #1
       [0, 0, 1, 0],  #2
       [0, 0, 1, 1],  #3
       [0, 1, 0, 0],  #4
       [0, 1, 0, 1],  #5
       [0, 1, 1, 0],  #6
       [0, 1, 1, 1],  #7
       [1, 0, 0, 0],  #8
       [1, 0, 0, 1],  #9
       [1, 0, 1, 0],  #A
       [1, 0, 1, 1],  #B
       [1, 1, 0, 0],  #C
       [1, 1, 0, 1],  #D
       [1, 1, 1, 0],  #E
       [1, 1, 1, 1]]  #F

def ascii_to_hex(c):
    # 9 이하
    if c <= '9':
        return ord(c) - ord('0')
    # 10 이상
    else:
        return ord(c) - ord('A') + 10

def hex_to_binary(x):
    global pos, t
    for i in range(4):
        t += str(asc[x][i])

T = int(input())
for tc in range(1, T+1):
    pos = -1
    t = ''
    N, amho = input().split()
    # print(amho)
    for i in range(len(amho)):
        hex_to_binary(ascii_to_hex(amho[i]))
    print('#{} {}'.format(tc, t))


# 정현님 코드 참조
# def hex_to_binary(x):
    # ans=''
    # for j in range(4):
    #     if num & (1 << j):
    #         ans = '1' + ans
    #     else:
    #         ans = '0' + ans
    # return ans