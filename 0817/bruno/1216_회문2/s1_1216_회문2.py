import sys
sys.stdin = open('input.txt')

def is_Palinedrome(string):
    for i in range(len(string)//2):
        if string[i] != string[-1-i]:
            return False
    return True

for _ in range(10):
    tc = int(input())
    square = [list(input()) for _ in range(100)]    # 행기준 2차원 리스트
    zip_square = list(zip(*square))                 # 열기준 2차원 리스트
    max_row = 0     # 행의 회문중 최대길이
    max_col = 0     # 열의 회문중 최대길이
    for i in range(100):
        for start in range(100):                    # 회문을 판단할 구간 시작점
            for end in range(1, 100 - start + 1):   # 회문을 판단할 구간 끝점
                len_row = 0                         # 행 회문의 길이
                if is_Palinedrome(square[i][start:start + end]):
                    len_row = len(square[i][start:start + end])
                    if len_row > max_row:           # 행 회문 최댓값 구하기
                        max_row = len_row

                len_col = 0                         # 열 회문의 길이
                if is_Palinedrome(zip_square[i][start:start + end]):
                    len_col = len(zip_square[i][start:start + end])
                    if len_col > max_col:           # 열 회문 최댓값 구하기
                        max_col = len_col
    print('#{} {}'.format(tc, max(max_row, max_col)))



