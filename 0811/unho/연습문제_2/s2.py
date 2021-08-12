'''

'''

import sys
sys.stdin = open('input2.txt')

test_case = int(input())


dr = [-1, 0, 1, 0]  # 상, 우, 하, 좌
dc = [0, 1, 0, -1]


for tc in range(1, test_case+1):
    num = int(input())
    board = [list(map(int, input().split())) for _ in range(num)]       # 2차원 배열
    answer = 0                                                          # 정답 변수

    for r in range(num):                                                # row 만큼 반복
        for c in range(num):                                            # column 만큼 반복
            for k in range(4):                                          # 상하좌우 4번 움직이므로 4번 반복
                nr = r + dr[k]                                          # 비교할 새로운 좌표
                nc = c + dc[k]
                if (0 <= nr < num) and (0 <= nc < num):                 # 새로운 좌표가 인덱스 범위 안일때만 실행
                    answer += abs(board[r][c] - board[nr][nc])          # 두 수 차이의 절대값을 누적



    print('#{} {}'.format(tc, answer))