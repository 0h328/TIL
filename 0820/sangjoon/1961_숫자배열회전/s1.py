# 문제 푼 시간
# 풀이법: 구현
import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


def rotate_90(lst: list, n: int):
    rotated_lst = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_lst[i][j] = lst[n - 1 - j][i]
    return rotated_lst


def rotate_180(lst: list, n: int):
    rotated_lst = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_lst[i][j] = lst[n - 1 - i][n - 1 - j]
    return rotated_lst


def rotate_270(lst: list, n: int):
    rotated_lst = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_lst[i][j] = lst[j][n - 1 - i]
    return rotated_lst


test_case = int(input())

for test in range(1, test_case + 1):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]

    lst_90 = rotate_90(lst, n)
    lst_180 = rotate_180(lst, n)
    lst_270 = rotate_270(lst, n)

    print(f"#{test}")
    for i in range(n):
        print("".join(map(str, lst_90[i])), end="")
        print(" ", end="")
        print("".join(map(str, lst_180[i])), end="")
        print(" ", end="")
        print("".join(map(str, lst_270[i])))
