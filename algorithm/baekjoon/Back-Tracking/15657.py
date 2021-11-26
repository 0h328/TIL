# N과 M(8)
from itertools import combinations_with_replacement
import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
cases = list(combinations_with_replacement(nums, M))
for case in cases:
    print(*case)
