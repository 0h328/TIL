import sys
sys.stdin = open('input.txt')
for _ in range(1, 11):
    tc = int(input())                                                # 테스트 케이스
    numbers = [list(map(int, input().split())) for _ in range(100)]  # 100 * 100 세팅

    max_sum = 0
    for i in range(100):              # row 합
        my_sum = 0
        for j in range(100):
            my_sum += numbers[i][j]   # 행 우선 탐색 & 행의 최댓값 갱신
        if my_sum > max_sum:
            max_sum = my_sum

    for i in range(100):              # column 합
        my_sum = 0
        for j in range(100):
            my_sum += numbers[j][i]   # 열 우선 탐색 & 열의 최댓값 갱신
        if my_sum > max_sum:
            max_sum = my_sum

    my_sum = 0
    for i in range(100):              # 좌상단 -> 우하단 diagonal
        my_sum += numbers[i][i]
    if my_sum > max_sum:
        max_sum = my_sum

    my_sum = 0                        # 우상단 -> 좌하단 diagonal
    for i in range(100):
        my_sum += numbers[i][99-i]
    if my_sum > max_sum:
        max_sum = my_sum

    print('#{} {}'.format(tc, max_sum))