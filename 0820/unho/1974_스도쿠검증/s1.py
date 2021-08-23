'''
1. 가로와 세로 확인하면 유일한 수인지 확인
2. 같은 크기의 9개 구역으로 나누어서 그 안에 숫자가 유일한 숫자들인지 확인
'''

import sys
sys.stdin = open('input.txt')



test_case = int(input())

for tc in range(1, test_case+1):
    board = [list(map(int, input().split())) for _ in range(9)]
    answer = 1

    for i in range(9):
        chk_row = [False] * 10                          # 가로에 숫자가 모두 다른지 체크를 위한 리스트
        chk_col = [False] * 10                          # 세로에 숫자가 모두 다른지 체크를 위한 리스트
        for j in range(9):
            chk_row[board[i][j]] = True                 # 숫자가 있으면 해당 인덱스 True
            chk_col[board[j][i]] = True                 # 숫자가 있으면 해당 인덱스 True

        if sum(chk_row) != 9 or sum(chk_col) != 9:      # True 는 1 이므로 9개 모두 있으면 True가 9개이므로 합이 9가 된다
            answer = 0
            break

    for i in range(0, 9, 3):                            # 사각형 9개의 구역으로 나눔
        for j in range(0, 9, 3):
            chk_square = [False] * 10                   # 사각형에 숫자가 모두 다른지 체크를 위한 리스트
            for y in range(3):
                for x in range(3):
                    chk_square[board[i+y][j+x]] = True  # 사각형 하나에 숫자가 있으면 해당 인덱스 True
            if sum(chk_square) != 9:
                answer = 0
                break

    print('#{} {}'.format(tc, answer))