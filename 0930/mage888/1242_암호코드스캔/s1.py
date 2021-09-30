import sys
sys.stdin = open('input.txt')

def erase(i, j, min_ratio):
    cnt = 0
    while bin_data[i][j] == 1:
        cnt += 1
    for r in range(i, cnt):
        for c in range(j-56*min_ratio+1, j+1):
            bin_data[r][c] = 0

hex_to_bin = {
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

ratio = {
    211: 0,
    221: 1,
    122: 2,
    411: 3,
    132: 4,
    231: 5,
    114: 6,
    312: 7,
    213: 8,
    112: 9,
}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    hex_data = [input() for _ in range(N)]
    bin_data = [[0] * (M*4) for _ in range(N)]

    for i in range(N):
        for j in range(M):
            for k in range(4):
                bin_data[i][j*4+k] += int(hex_to_bin[hex_data[i][j]][k])

    M *= 4
    for i in range(N):
        j = M-1
        num_list = [0] * 8
        k = 0 # 찾은 암호숫자의 개수
        while j > 0:
            while j >= 0 and bin_data[i][j] == 0:
                j -= 1
            c1 = 0
            if k == 0:
                col = j
            while j >= 0 and bin_data[i][j] == 1:
                c1 += 1
                j -= 1
            c2 = 0
            while j >= 0 and bin_data[i][j] == 0:
                c2 += 1
                j -= 1
            c3 = 0
            while j >= 0 and bin_data[i][j] == 1:
                c3 += 1
                j -= 1
            if c1 > 0:
                min_ratio = min(c1, c2, c3)
                # 0001101 ( 2:1:1 -> 211 = c3c2c1 )
                num_list[7-k] = ratio[c3//min_ratio * 100 + c2//min_ratio * 10 + c1//min_ratio]
                k += 1
                if k == 8:
                    erase(i, col, min_ratio)


        # odd_num = 0
        # even_num = 0
        # ans = 0
        # for t in range(len(num_list)):
        #     if t % 2:
        #         odd_num += num_list[t] * 3
        #     else:
        #         even_num += num_list[t]
        #
        # ans = odd_num + even_num
        #
        # if ans % 10 == 0:
        #     print('#{} {}'.format(tc, sum(num_list)))
        # else:
        #     print('#{} 0'.format(tc))







