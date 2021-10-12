import sys
sys.stdin = open('input.txt')
from itertools import combinations

T = int(input())
for t in range(1, T+1):
    N, B = map(int, input().split())    # N : 점원수, B : 선반높이
    H = list(map(int, input().split()))     # 점원 키
    success = []
    for i in range(1, N+1):
        c = list(combinations(H, i))
        for j in c:
            if sum(j) >= B:
                success.append(sum(j))
    success.sort()
    print('#{} {}'.format(t, success[0] - B))
