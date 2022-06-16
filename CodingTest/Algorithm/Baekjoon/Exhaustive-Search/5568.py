import sys
from itertools import permutations
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
cards = [sys.stdin.readline().rstrip() for _ in range(n)]

ans = set()
for i in permutations(cards, k):
    ans.add(''.join(i))

print(len(ans))