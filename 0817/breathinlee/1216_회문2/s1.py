import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    tc = int(input())
    row_arr = [input() for _ in range(100)]
    max_palindrome = 1

    # 행별로 탐색
    for i in range(100):
        for j in range(2, 100):                                 # 회문 길이 범위
            for k in range(100-j+1):
                for l in range(j//2):                            # 중간 기점으로 앞뒤 비교
                    if row_arr[i][k+l] != row_arr[i][k+j-1-l]:
                        break
                else:                                            # 회문인 경우
                    if max_palindrome <= j:
                        max_palindrome = j

    # 열별로 탐색
    for i in range(100):
        for j in range(2, 100):                                  # 회문 길이 범위
            for k in range(100-j+1):
                for l in range(j//2):
                    if row_arr[k+l][i] != row_arr[k+j-1-l][i]:
                        break
                else:                                            # 회문인 경우
                    if max_palindrome <= j:
                        max_palindrome = j


    print('#{} {}'.format(tc, max_palindrome))