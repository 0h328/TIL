# 문제 푼 시간
# 풀이법: 정렬, 구현
import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


def check_sudoku(lst: list):
    check = [i for i in range(1, 10)]

    # check row & col
    for i in range(9):
        row = []
        for j in range(9):
            row.append(lst[j][i])
        col = lst[i]
        if sorted(row) != check or sorted(col) != check:
            return 0

    # check cube
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            cube = []
            cube += lst[i][j : j + 3]
            cube += lst[i + 1][j : j + 3]
            cube += lst[i + 2][j : j + 3]
            if sorted(cube) != check:
                return 0

    return 1


test_case = int(input())
for test in range(1, test_case + 1):
    lst = [list(map(int, input().split())) for _ in range(9)]
    ans = check_sudoku(lst)

    print("#{} {}".format(test, ans))