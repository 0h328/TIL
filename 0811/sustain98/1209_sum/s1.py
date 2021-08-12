import sys
sys.stdin = open('input.txt')

for _ in range(10):
    idx = input()
    l = [list(map(int, input().split())) for _ in range(100)]

    max_sum = 0
    right_down = 0
    right_up = 0
    for i in range(100):
        right_down += l[i][i]                           #우하향 대각선의 합을 누적
        right_up += l[99-i][i]                          #우상향 대각선의 합을 누적
        tmp_row = 0
        tmp_col = 0
        for j in range(100):
            tmp_col += l[j][i]
            tmp_row += l[i][j]
        max_sum = max(tmp_col, tmp_row, max_sum)         #행/열 합 비교
    max_sum = max(max_sum, right_down, right_up)         #대각선들의 합과 행/열들이 합의 최대중 가장 큰 값을 max_sum에 할당
    print('#{} {}'.format(idx, max_sum))