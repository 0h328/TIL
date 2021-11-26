import sys
sys.stdin=open('input.txt')

from heapq import heappush, heappop


def dijkstra(s, grp):  # 다익스트라
    q = [(0, s)]
    dp = [INF] * (N + 1)

    while q:
        d, n = heappop(q)

        if dp[n] < d: continue

        for nn, nd in grp[n].items():
            x = nd + d
            if dp[nn] > x:
                dp[nn] = x
                heappush(q, (x, nn))
    return dp


ans = []
INF = 10 ** 5
T = int(input())
for tc in range(1, T + 1):
    N, M, X = map(int, input().split())

    grp1 = [{} for _ in range(N + 1)]  # 입력 자체의 단방향 그래프
    grp2 = [{} for _ in range(N + 1)]  # 입력 반대의 단방향 그래프

    for _ in range(M):
        a, b, c = map(int, input().split())
        if b in grp1[a]:
            grp1[a][b] = min(grp1[a][b], c)
            grp2[b][a] = min(grp1[b][a], c)
        else:
            grp1[a][b] = c
            grp2[b][a] = c

    dp1 = dijkstra(X, grp1)  # 정상 방향의 다익스트라
    dp2 = dijkstra(X, grp2)  # 반대 방향의 다익스트라
    ans.append('#{} {}'.format(tc, max([dp1[i] + dp2[i] for i in range(1, N + 1) if i != X])))  # 두 방향의 최대값(단, X번째는 제외)

print(*ans, sep='\n')
