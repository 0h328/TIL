import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    tc = int(input())
    row_arr = [input() for _ in range(100)]
    max_palindrome = 1

    # 행 고려
    for i in range(100):                                         # 행
        for j in range(1, 100):                                  # 회문 길이 범위
            for k in range(100-j+1):                             # 열
                for l in range(j//2):
                    if row_arr[i][k+l] != row_arr[i][k+j-1-l]:
                        break
                else:                                            # 회문인 경우
                    if max_palindrome <= j:
                        max_palindrome = j

    # 열 고려
    for i in range(100):                                         # 열
        for j in range(1, 100):                                  # 회문 길이 범위
            for k in range(100-j+1):                             # 행
                for l in range(j//2):
                    if row_arr[k+l][i] != row_arr[k+j-1-l][i]:
                        break
                else:                                            # 회문인 경우
                    if max_palindrome <= j:
                        max_palindrome = j


    print('#{} {}'.format(tc, max_palindrome))