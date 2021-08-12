import sys
sys.stdin = open("input.txt")

for tc in range(10):
    T = int(input())                # 각 테스트 케이스의 번호
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_sum = 0

    for i in range(100):            # 각 행들의 합 고려하기 위해
        max_val = 0
        for j in range(100):
            max_val += arr[i][j]
            if max_sum < max_val:
                max_sum = max_val

    for i in range(100):            # 각 열들의 합 고려하기 위해
        max_val = 0
        for j in range(100):
            max_val += arr[j][i]
            if max_sum < max_val:
                max_sum = max_val

    for i in range(100):            # 대각선의 합 고려하기 위해
        max_val = 0
        max_val += arr[i][i]
        if max_sum < max_val:
            max_sum = max_val

    for i in range(100):             # / 대각선(opposite diagonal)의 합 고려하기 위해
        max_val = 0
        max_val += arr[i][99-i]
        if max_sum < max_val:
            max_sum = max_val

    print('#{} {}'.format(T, max_sum))
