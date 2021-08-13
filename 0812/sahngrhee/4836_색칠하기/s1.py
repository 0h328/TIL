import sys
sys.stdin = open('input.txt')
from pandas import DataFrame

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    my_info = [list(map(int, input().split())) for _ in range(N)]
    arr1 = [[0] * 10 for _ in range(10)]
    arr2 = [[0] * 10 for _ in range(10)]
    arr3 = [[0] * 10 for _ in range(10)]

    for my_list in my_info:
        if my_list[-1] == 1:
            for r in range(my_list[0], my_list[2]+1):
                for c in range(my_list[1], my_list[3]+1):
                    arr1[r][c] = 1

        if my_list[-1] == 2:
            for r in range(my_list[0], my_list[2]+1):
                for c in range(my_list[1], my_list[3]+1):
                    arr2[r][c] = 2

    for r in range(10):
        for c in range(10):
            arr3[r][c] = arr1[r][c] + arr2[r][c]

    ans = 0
    for r in range(10):
        for c in range(10):
            if arr3[r][c] == 3:
                ans += 1

    print('#{} {}'.format(test_case, ans))


