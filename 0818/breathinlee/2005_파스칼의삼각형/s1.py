import sys
sys.stdin = open("input.txt")


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    # print(arr)
    for i in range(N):
        for j in range(i+1):
            if j == 0 or j == i:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    print('#{}'.format(tc))
    for i in range(tc):
        print(*arr[i][0:i+1])

