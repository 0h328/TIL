def perm(k, N, total):
    global ans
    if total <= ans:                                       # 가지치기
        return
    if N == k:
        ans = max(total, ans)                              # 최댓값 갱신
        return
    else:
        for i in range(k, N):                              # 조합 생성
            things[i], things[k] = things[k], things[i]
            perm(k+1, N, total*data[k][things[k]] / 100)
            things[i], things[k] = things[k], things[i]

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    ans = 0
    things = list(range(16))
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    perm(0, N, 1)
    print('#{} {:.6f}'.format(tc, ans*100))