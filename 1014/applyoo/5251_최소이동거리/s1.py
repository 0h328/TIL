import sys
sys.stdin=open('input.txt')


from heapq import heappush, heappop


def bfs():
    q = [(0, 0)]
    DP = [INF] * (N+1)
    DP[0] = 0

    while q:
        w, n = heappop(q)

        if DP[n] < w: continue

        for nn, nw in grp[n].items():
            if DP[nn] > w + nw:
                DP[nn] = w + nw
                heappush(q, (w+nw, nn))
    return DP[-1]


ans = []
INF = 10**5
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    grp = [{} for _ in range(N+1)]
    for _ in range(M):
        s, e, w = map(int, input().split())
        if e in grp[s]: grp[s][e] = min(grp[s][e], w)
        else: grp[s][e] = w

    ans.append('#{} {}'.format(tc, bfs()))
print(*ans, sep='\n')
