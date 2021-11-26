def find_set(x):
    if x == p[x]:
        return x
    p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    global ans
    a = find_set(x)
    b = find_set(y)
    if a == b: return                   # 대표자가 같은 경우 종료
    p[b] = a
    ans -= 1

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    # N: 정점 / M: 간선
    N, M = map(int, input().split())
    ans = N
    p = [i for i in range(N+1)]

    for _ in range(M):
        u, v = map(int, input().split())
        union(u, v)

    # print('#{} {}'.format(tc, ans))
    print('#{} {}'.format(tc, len(set(p))-1))  # 중복 제거 후 0 제외