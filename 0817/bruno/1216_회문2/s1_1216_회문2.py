import sys
sys.stdin = open('input.txt')

def is_Palinedrome(string):
    for i in range(len(string)//2):
        if string[i] != string[-1-i]:
            return False
    return True

for _ in range(10):
    tc = int(input())
    square = [list(input()) for _ in range(100)]
    zip_square = list(zip(*square))
    max_row = 0
    max_col = 0
    for i in range(100):
        for start in range(100):
            for end in range(1, 100 - start + 1):
                len_row = 0
                if is_Palinedrome(square[i][start:start + end]):
                    len_row = len(square[i][start:start + end])
                    if len_row > max_row:
                        max_row = len_row

                len_col = 0
                if is_Palinedrome(zip_square[i][start:start + end]):
                    len_col = len(zip_square[i][start:start + end])
                    if len_col > max_col:
                        max_col = len_col
    print('#{} {}'.format(tc, max(max_row, max_col)))



