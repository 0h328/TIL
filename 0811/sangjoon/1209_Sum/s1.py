import sys

sys.stdin = open("input.txt")


test_case = 10

for test in range(1, test_case + 1):
    test = int(input())
    lst = [list(map(int, input().split())) for _ in range(100)]
    ans = 0
    diagonal_r, diagonal_l = 0, 0
    for i in range(100):
        diagonal_r += lst[i][99 - i]
        diagonal_l += lst[99 - 1][i]
        row, col = 0, 0
        for j in range(100):
            row += lst[i][j]
            col += lst[j][i]

        if row > ans:
            ans = row
        if col > ans:
            ans = col

    if diagonal_r > ans:
        ans = diagonal_r
    if diagonal_l > ans:
        ans = diagonal_l

    print("#{} {}".format(test, ans))