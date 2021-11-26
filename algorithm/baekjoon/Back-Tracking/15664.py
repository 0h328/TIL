# N과 M(10)
from itertools import combinations
import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
for answer in sorted(set(list(combinations(nums, M)))):
    print(*answer)
