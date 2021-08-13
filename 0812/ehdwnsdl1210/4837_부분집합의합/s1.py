import sys
sys.stdin = open('input.txt')
from itertools import combinations

T = int(input())
A = []
for i in range(1, 13):
    A.append(i)

for tc in range(T):

    N, K = list(map(int, input().split()))

    result = list(combinations(A, N))

    cnt = 0

    for i in result:
        if sum(list(i)) == K:
            cnt += 1

    print('#{} {}'.format(tc + 1, cnt))