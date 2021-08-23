import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

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

                # 이미 사용한 숫자라면 멈춰
                if row[num_row]:
                    return 0
                row[num_row] = 1

                if col[num_col]:
                    return 0
                col[num_col] = 1

                # 3*3
                if i % 3 == 0 and j % 3 == 0:
                    square = [0] * 10
                    for r in range(i, i+3):
                        for c in range(j, j+3):
                            num = sudoku[r][c]
                            # 중복이면 그만!
                            if square[num]:
                                return 0
                            square[num] = 1
        return 1

    print('#{} {}'.format(tc, check()))

# 가로 / 세로 / 3*3 합이 45(이건 안된다)
# 0~9 3으로 나눠 나머지 0  0,3,6