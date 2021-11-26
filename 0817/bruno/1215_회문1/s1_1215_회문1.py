import sys
sys.stdin = open('input.txt')

def is_Palinedrome(string):
    for i in range(len(string)//2):
        if string[i] != string[-1-i]:
            return False
    return True

for tc in range(1, 11):
    M = int(input())
    square = [list(input()) for _ in range(8)]
    zip_square = list(zip(*square))
    cnt = 0
    for i in range(8):
        for j in range(8 - M + 1):
            if is_Palinedrome(square[i][j:j+M]):
                cnt += 1
            if is_Palinedrome(zip_square[i][j:j+M]):
                cnt += 1
    print('#{} {}'.format(tc, cnt))
