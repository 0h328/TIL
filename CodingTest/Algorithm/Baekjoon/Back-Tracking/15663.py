# N과 M(9)
from itertools import permutations
import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
nums = sorted(list((map(int, input().split()))))
cases = list(permutations(nums, M))
sub = []

for case in cases:
    sub.append(case)

answer = sorted(list(set(sub)))
for ans in answer:
    print(*ans)
