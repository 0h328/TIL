# 문제 설계
# 문제 풀이
# 디버깅 (정답 유무)

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    N, M = map(int, input().split())        # A는 행/열, B는 회문길이
    row_pal = [input() for _ in range(N)]
    pal_list = []

    # 행 회문 찾기
    for i in range(N):
        for j in range(N-M+1):
            if row_pal[i][j:j+M] == row_pal[i][j:j+M][::-1]:
                pal_list.append(row_pal[i][j:j+M])

    # 열 회문 찾기
    col_pal = list(zip(*row_pal))

    for i in range(N):
        for j in range(N-M+1):
            if col_pal[i][j:j+M] == col_pal[i][j:j+M][::-1]:
                pal_list.append(''.join(col_pal[i][j:j+M]))

    print('#{} {}'.format(tc, *pal_list))
