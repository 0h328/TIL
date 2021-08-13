import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    my_sum_list = []
    for i in range(0, N-M+1):
        for j in range(0, N-M+1):
            my_sum = 0
            for r in range(i, i+M):
                for c in range(j, j+M):
                    my_sum += arr[r][c]
            my_sum_list.append(my_sum)
    ans = max(my_sum_list)

    print('#{} {}'.format(test_case, ans))