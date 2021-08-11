import sys

sys.stdin = open("input.txt")


# 1. 행우선
def read_row(lst: list):
    for i in range(n):
        for j in range(n):
            print(lst[i][j], end=" ")
    print()


# 2. 열우선
def read_col(lst: list):
    for i in range(n):
        for j in range(n):
            print(lst[j][i], end=" ")
    print()


# 3. 지그재그
def read_zigzag(lst: list):
    for i in range(n):
        for j in range(n):
            print(lst[i][j + (-1 - (2 * j)) * (i % 2)], end=" ")
    print()


# 4. 전치행렬
def transpose_matrix(lst: list):
    transpose_lst = lst[:]
    for i in range(n):
        for j in range(n):
            if i > j:
                transpose_lst[i][j], transpose_lst[j][i] = transpose_lst[j][i], transpose_lst[i][j]
    print(transpose_lst)


n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
read_row(lst)
read_col(lst)
read_zigzag(lst)
transpose_matrix(lst)