from itertools import combinations

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    min_val = 20001

    for comb in combinations(range(N), N//2):
        case_A = list(comb)
        case_B = list(set(range(N))-set(comb))

        res_A = 0
        res_B = 0

        for i, j in combinations(case_A, 2):
            res_A += S[i][j] + S[j][i]
        for i, j in combinations(case_B, 2):
            res_B += S[i][j] + S[j][i]

        ans = abs(res_A - res_B)

        if ans < min_val:
            min_val = ans

    print('#{} {}'.format(tc, min_val))