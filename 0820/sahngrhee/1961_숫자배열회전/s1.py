import sys
sys.stdin = open('input.txt')

def rotate(arr):
    F = []
    for c in range(N):
        f = []
        for r in range(N - 1, -1, -1):
            f.append(arr[r][c])
        F.append(f)
    return F


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    r_90 = rotate(arr)
    r_180 = rotate(r_90)
    r_270 = rotate(r_180)
    result = []
    result.append(r_90)
    result.append(r_180)
    result.append(r_270)

    print('#{}'.format(test_case))
    for i in range(N):
        for k in range(len(result)):
            if k != 0: print(end=' ')
            for j in range(N):
                print(result[k][i][j], end='')
        print()

    # print('#{}'.format(test_case))
    # for i in range(N):
    #     for k in range(1, 4):
    #         if k != 1: print(end=' ')
    #         for j in range(N):
    #             print(arr[k][i][j], end='')
    #     print()




