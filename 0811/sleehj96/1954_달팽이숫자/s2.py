import sys

sys.stdin = open('input.txt')

T = int(input())
idx = 1

while idx <= T:
    n = int(input())

    ans_list = [[0] * n for _ in range(n)]
    d = 0
    r = c = 0
    input_in_row = n

    num = 1
    while num <= n*n:
        if d == 0:
            for i in range(input_in_row):
                ans_list[r][c+i] = num
                num += 1
            else:
                r += 1
                c += i

        if d == 1:
            for i in range(input_in_row):
                ans_list[r+i][c] = num
                num += 1
            else:
                r += i
                c -= 1

        if d == 2:
            for i in range(input_in_row):
                ans_list[r][c-i] = num
                num += 1
            else:
                r -= 1
                c -= i

        if d == 3:
            for i in range(input_in_row):
                ans_list[r-i][c] = num
                num += 1
            else:
                r -= i
                c += 1

        d = (d + 1) % 4

        if d & 1:
            input_in_row -= 1

    print('#{}'.format(idx))

    for i in range(n):
        for j in range(n):
            print(ans_list[i][j], end=' ')
        print()

    idx += 1
