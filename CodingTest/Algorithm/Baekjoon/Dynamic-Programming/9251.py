# LCS = Longest Common Subsequence (최장 공통 부분 문자열)
# ACAYKP와 CAPCAK의 최장 공통 부분 문자열은 ACAK
# 1. 기준 문자열에서 첫 idx부터 뽑고, 비교할 문자열에서 앞에서부터 한 글자씩 뽑아 비교한다.
# 2. dp 라는 (기존 문자열 길이) x (비교 문자열 길이)로 2차원 배열을 만든다.
# 3. 두 문자열이 같다면 해당 idx에 +1을 넣어준다
# 4. 두 문자열이 다르면 해당 idx 기준 위의 idx와 왼쪽 idx 중 큰 값을 넣어준다.
# 5. 완성된 2차원 배열의 마지막 행과 열의 idx 값을 출력한다.

#   0 A C A Y K P
# 0 0 0 0 0 0 0 0
# C 0 0 1 1 1 1 1
# A 0 1 1 2 2 2 2
# P 0 1 1 2 2 2 3
# C 0 1 2 2 2 2 3
# A 0 1 2 3 3 3 3
# K 0 1 2 3 3 4 4

import sys
sys.stdin = open('input.txt')

str_1 = list(input())
str_2 = list(input())
dp = [[0 for _ in range(len(str_1)+1)] for _ in range(len(str_2)+1)]

for i in range(1, len(str_2)+1):
    for j in range(1, len(str_1)+1):
        if str_1[j-1] == str_2[i-1]:                # 같으면
            dp[i][j] = dp[i-1][j-1] + 1             # 해당 idx에 +1
        else:                                       # 다르면
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])  # 왼 idx와 위 idx 중 큰 값을 갱신

print(dp[-1][-1])