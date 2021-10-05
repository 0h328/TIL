import sys
sys.stdin = open('input.txt')
from pandas import DataFrame

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [[0] * 25 for _ in range(N)]
    for i in range(N):
        start, end = map(int, input().split())
        for j in range(start, end+1):
            arr[i][j] = 1

    print(DataFrame(arr))