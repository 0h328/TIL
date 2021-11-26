import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    data = [list(map(int, input().split())) for _ in range(9)]

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ans = 1

    for i in range(9):
        temp_row = []
        for j in range(9):
            temp_row.append(data[i][j])

        if nums != sorted(temp_row):
            ans = 0
        break

    for i in range(9):
        temp_col = []
        for j in range(9):
            temp_col.append(data[j][i])

        if nums != sorted(temp_col):
            ans = 0
        break

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):

            temp_sq = []

            for k in range(i, i+3):
                for l in range(j, j+3):
                    temp_sq.append(data[k][l])

            if nums != sorted(temp_sq):
                ans = 0
                break

    print(ans)