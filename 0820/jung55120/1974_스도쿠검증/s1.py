import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    print(arr)
    # [[7, 3, 6, 4, 2, 9, 5, 8, 1],
    #  [5, 8, 9, 1, 6, 7, 3, 2, 4],
    #  [2, 1, 4, 5, 8, 3, 6, 9, 7],
    #  [8, 4, 7, 9, 3, 6, 1, 5, 2],
    #  [1, 5, 3, 8, 4, 2, 9, 7, 6],
    #  [9, 6, 2, 7, 5, 1, 8, 4, 3],
    #  [4, 2, 1, 3, 9, 8, 7, 6, 5],
    #  [3, 9, 5, 6, 7, 4, 2, 1, 8],
    #  [6, 7, 8, 2, 1, 5, 4, 3, 9]]

    for i in range(1, 9):
        min_idx = i
        for j in range(min_idx+1, 9):
            if arr[i-1][j-1] > arr[i-1][j]:
                min_idx = j
                arr[i-1][j-1], arr[i-1][j] = arr[i-1][j], arr[i-1][j-1]
    print(arr)