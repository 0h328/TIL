import sys
sys.stdin = open('input.txt')

def cnt_palindrome(chars, M):
    cnt = 0
    # 행 별로 확인
    for i in range(8):
        for j in range(8 - M + 1):
            for m in range(M // 2): #앞뒤로 하나씩 일치여부 확인
                if chars[i][j + m] != chars[i][j + M - 1 - m]:
                    break
            else:
                cnt += 1
    # 열 별로 확인
    for i in range(8):
        for j in range(8 - M + 1):
            for m in range(M // 2): #앞뒤로 하나씩 일치여부 확인
                if chars[j + m][i] != chars[j + M - 1 - m][i]:
                    break
            else:
                cnt += 1
    return cnt

for t in range(1, 11):
    M = int(input())
    chars = [list(input()) for _ in range(8)]
    print('#{} {}'.format(t, cnt_palindrome(chars, M)))