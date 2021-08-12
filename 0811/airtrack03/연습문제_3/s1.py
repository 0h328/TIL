# 내장 함수 사용
import sys
from itertools import combinations

sys.stdin = open('input.txt')

data = list(map(int, input().split()))
N = len(data)
ans = []

for i in range(N+1):
    ans.extend(combinations(data, i))

for combi in ans:
    if combi:
        print(' '.join(list(map(str, combi))))
    else:
        print()