import sys
# from pandas import DataFrame
sys.stdin = open('input.txt')

T = int(input())
test_case = 1

while test_case <= T:

    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    r = c = 1

    # print(DataFrame(data))

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    ans = 0

    for i in range(N):

        for j in range(N):

            # print(data[i][j])

            for k in range(4):

                if 0 <= i+dr[k] < N and 0 <= j+dc[k] < N:
                    # print(data[i+dr[k]][j+dc[k]])
                    ans += abs(data[i][j] - data[i+dr[k]][j+dc[k]])

    print('#{} {}'.format(test_case, ans))

    test_case += 1


