import sys
sys.stdin = open('input2.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    result = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                if -1 < i + dy[k] < N and -1 < j + dx[k] < N :
                    result += abs(arr[i + dy[k]][j + dx[k]] - arr[i][j])
    print('#{} {}'.format(test_case, result))
