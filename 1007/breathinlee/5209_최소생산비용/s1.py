"""
봄부터 새로 생산되는 N종의 제품을 N곳의 공장에서 한 곳당 한가지씩 생산
"""

# 런타임에러
from itertools import permutations
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    min_result = 987654321

    for cases in permutations([n for n in range(N)]):
        idx = 0
        result = 0
        for case in cases:
            result += cost[idx][case]
            idx += 1
            if min_result <= result:
                break

        if min_result >= result:
            min_result = result

    print('#{} {}'.format(tc, min_result))

