import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    red = [[0] * 10 for _ in range(10)]
    blue = [[0] * 10 for _ in range(10)]
    cnt = 0
    for i in range(N):
        if arr[i][4] == 1:
            for j in range(arr[i][0], arr[i][2] + 1):
                for k in range(arr[i][1], arr[i][3] + 1):
                    red[j][k] = 1
        else:
            for j in range(arr[i][0], arr[i][2] + 1):
                for k in range(arr[i][1], arr[i][3] + 1):
                    blue[j][k] = 1

    for i in range(10):
        for j in range(10):

            if red[i][j] & blue[i][j]:
                cnt += 1
    print('#{} {}'.format(test_case, cnt))