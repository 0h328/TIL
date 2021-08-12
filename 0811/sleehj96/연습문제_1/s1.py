import sys

sys.stdin = open('input.txt')

n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))


def row_first(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            print(lst[i][j], end=' ')
    print()


def col_first(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            print(lst[j][i], end=' ')
    print()


def zigzag(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            print(lst[i][len(lst)-j-1 if i % 2 else j], end=' ')
    print()


def transpose(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            lst[i][j], lst[j][i] = lst[j][i], lst[i][j]
    print(lst)


row_first(arr)
col_first(arr)
zigzag(arr)
transpose(arr)