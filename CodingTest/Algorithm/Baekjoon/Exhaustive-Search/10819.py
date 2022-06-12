import sys
from itertools import permutations
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

tmp = permutations(nums)    # 모든 순열의 경우의 수
ans = 0

for i in tmp:
    d = 0
    for j in range(len(i)-1):
        d += abs(i[j]-i[j+1])

    if d > ans:
        ans = d

print(ans)
