def check():
    for i in range(9):
        # 체크를 위한
        row = [0] * 10
        col = [0] * 10

        for j in range(9):
            # 행 검사
            num_row = sudoku[i][j]
            # 열 검사
            num_col = sudoku[j][i]

            # 이미 존재하는 경우는 바로 종료
            if row[num_row]:
                return 0
            if col[num_col]:
                return 0

            row[num_row] = 1
            col[num_col] = 1

            ########################
            # 3 * 3 검사도 한번에 처리
            if i % 3 == 0 and j % 3 == 0:
                square = [0] * 10
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        num = sudoku[r][c]
                        # 중복된 숫자가 나오면 끝
                        if square[num]:
                            return 0
                        sudoku[num] = 1
    return 1

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    print('#{} {}'.format(tc, check()))