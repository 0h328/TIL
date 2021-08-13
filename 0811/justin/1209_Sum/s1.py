import sys
sys.stdin = open('input.txt')
for _ in range(1, 11):
    tc = int(input())                                               # 테스트 케이스
    data = [list(map(int, input().split())) for _ in range(100)]    # 100 * 100 세팅

    max_sum = 0
    for i in range(100):       # row
        row_sum = 0
        for j in range(100):
            row_sum += data[i][j]
        if row_sum > max_sum:
            max_sum = row_sum

    for i in range(100):       # col
        col_sum = 0
        for j in range(100):
            col_sum += data[j][i]
        if col_sum > max_sum:
            max_sum = col_sum

    dia1_sum = 0
    for i in range(100):       # dia1
        dia1_sum += data[i][i]
    if dia1_sum > max_sum:
        max_sum = dia1_sum

    dia2_sum = 0
    for i in range(100):       # dia2
        dia2_sum += data[i][99-i]
    if dia2_sum > max_sum:
        max_sum = dia2_sum

    print('#{} {}'.format(tc, max_sum))