# N과 M(4)
from itertools import combinations_with_replacement

import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
cases = list(combinations_with_replacement(list(range(1, N+1)), M))

for case in cases:
    print(*case)
