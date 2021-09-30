import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    data = [list(input()) for _ in range(N)]

    code = ''
    info_reverse = []
    for i in range(N-1, -1, -1):
        for j in range(M-1, -1, -1):
            if data[i][j] == '1' and len(code) != 7:
                code = code+data[i][j]+data[i][j-1]+data[i][j-2]+data[i][j-3]+data[i][j-4]+data[i][j-5]+data[i][j-6]
                data[i][j] = '0'
                data[i][j-1] = '0'
                data[i][j-2] = '0'
                data[i][j-3] = '0'
                data[i][j-4] = '0'
                data[i][j-5] = '0'
                data[i][j-6] = '0'
                info_reverse.append(code)
                code = ''
            if len(info_reverse) == 8:
                break

    info = []
    for num_reverse in info_reverse:
        info.append(num_reverse[::-1])

    num_list = []
    for num in info:
        if num == '0001101':
            num_list.append(0)
        elif num == '0011001':
            num_list.append(1)
        elif num == '0010011':
            num_list.append(2)
        elif num == '0111101':
            num_list.append(3)
        elif num == '0100011':
            num_list.append(4)
        elif num == '0110001':
            num_list.append(5)
        elif num == '0101111':
            num_list.append(6)
        elif num == '0111011':
            num_list.append(7)
        elif num == '0110111':
            num_list.append(8)
        else:
            num_list.append(9)

    odd_num = 0
    even_num = 0
    ans = 0
    for i in range(len(num_list)):
        if i % 2:
            odd_num += num_list[i]*3
        else:
            even_num += num_list[i]

    ans = odd_num + even_num

    if ans % 10 == 0:
        print('#{} {}'.format(tc, sum(num_list)))
    else:
        print('#{} 0'.format(tc))