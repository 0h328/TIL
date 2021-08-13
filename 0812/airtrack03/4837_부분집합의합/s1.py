import sys
from itertools import combinations
sys.stdin = open('input.txt')

T = int(input())
data = list(range(1, 13))

for tc in range(1, T+1):
    # N: 부분집합의 원소의 개수, K: 합이 K인 부분집합
    N, K = map(int, input().split())
    ans = 0
    # subsets = list(combinations(data, N))
    #
    # for subset in subsets:
    #     if sum(subset) == K:
    #         ans += 1
    #
    # print('#{} {}'.format(tc, ans))

    for i in range((1<<N) - 1, 1<<12): # 원소 개수 N개인 부분집합
        temp = 0    # 부분집합 합을 저장할 변수
        cnt = 0
        for j in range(12):  # 부분집합의 원소들을 하나씩 temp에 더함
            if i & (1 << j):
                temp += data[j]
                cnt += 1
        if temp == K and cnt == N:   # 부분집합의 K인지 판단
            ans += 1

    print('#{} {}'.format(tc, ans))

