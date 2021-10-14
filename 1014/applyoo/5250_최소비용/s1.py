import sys
sys.stdin=open('input.txt')


from heapq import heappush, heappop


def bfs():
    q = [(0, 0, 0)]
    DP = [[INF] * N for _ in range(N)]
    DP[0][0] = 0

    while q:
        o, x, y = heappop(q)

        if DP[x][y] < o: continue

        for nx, ny in ((x-1, y), (x, y+1), (x+1, y), (x, y-1)):
            if (-1<nx<N) and (-1<ny<N):
                oo = max(A[nx][ny]-A[x][y], 0) + 1 + o
                if DP[nx][ny] > oo:
                    DP[nx][ny] = oo
                    heappush(q, (oo, nx, ny))
    return DP[-1][-1]


ans = []
INF = 10**5
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans.append('#{} {}'.format(tc, bfs()))
print(*ans, sep='\n')
