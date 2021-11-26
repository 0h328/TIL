import sys
from pandas import DataFrame


# 한 줄에서 가장 긴 palindrome의 길이를 반환
def max_palindrome_len(lst, n):

    i = len(lst)    # 탐색할 길이
    while i > n:    # 최대가 필요하므로 큰 수에서 작은 수로 가면서 탐색

        for j in range(0, len(lst) - i + 1):    # 해당 길이만큼 순회할 첫번째 인덱스

            # 회문 검사
            for k in range(0, i//2):            # 길이의 반 만큼만 순회하면 되므로 //2
                if lst[j + k] != lst[j+i-1-k]:  # 중간에 다른 값이 나오면 회문이 아님
                    break

            else:           # 전부 다 돌면 회문
                return i    # 그 때 해당하는 길이를 리턴
        i -= 1
    return n


sys.stdin = open('input.txt')

T = 10
case_num = 1
while case_num <= T:
    int(input())
    letter_grid = [list(input()) for _ in range(100)]
    # print(DataFrame(letter_grid))

    ans = 0
    # print(letter_grid)

    # 행별 탐색
    for letter in letter_grid:
        ans = max_palindrome_len(letter, ans)
        # if ans < max_len1:
        #     ans = max_len1

    # 열별 탐색
    for tp_letter in zip(*letter_grid):
        ans = max_palindrome_len(tp_letter, ans)
        # if ans < max_len2:
        #     ans = max_len2

    print('#{0} {1}'.format(case_num, ans))
    break
    case_num += 1
