import sys
sys.stdin = open('input.txt')
def change(arr):
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result[j][N-i-1] = arr[i][j]
    return result


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result_90 = change(arr)
    result_180 = change(result_90)
    result_270 = change(result_180)
    data = []
    for i in range(N):
        for j in range(N):
            data.append(result_90[i][j])
        for j in range(N):
            data.append(result_180[i][j])
        for j in range(N):
            data.append(result_270[i][j])
    print('#{}'.format(test_case))
    for k in range(len(data)):
        if k % (3*N) == 0 and k != 0:
            print()
        elif k % N == 0 and k !=0:
            print(' ', end='')
        print(data[k], end='')
    print()