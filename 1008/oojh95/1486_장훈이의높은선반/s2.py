import sys
from itertools import combinations
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    n = len(height)
    result = 200000
    for i in range(1, n+1):
        tmp = list(combinations(height, i))
        for k in range(len(tmp)):
            if sum(tmp[k]) >= B and sum(tmp[k]) - B < result:
                result = sum(tmp[k]) - B
    print('#{} {}'.format(tc, result))

