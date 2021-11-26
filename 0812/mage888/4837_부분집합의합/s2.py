import sys
from itertools import combinations
sys.stdin = open('input.txt')

T = int(input())
data = list(range(1, 13))

for tc in range(1, T+1):
    # N: 부분집합의 원소의 개수, K: 합이 K인 부분집합
    N, K = map(int, input().split())
    ans = 0
    subsets = list(combinations(data, N))
    print(subsets)

    for subset in subsets:
        if sum(subset) == K:
            ans += 1

    print('#{} {}'.format(tc, ans))