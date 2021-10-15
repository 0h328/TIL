import sys
sys.stdin=open('input.txt')

from heapq import heappush, heappop


def dijkstra(x, y):  # 다익스트라
    q = [(0, x, y)]
    dp = [[INF] * N for _ in range(N)]
    dp[x][y] = 0

    while q:
        d, x, y = heappop(q)

        if dp[x][y] < d: continue

        for nx, ny in ((x-1, y), (x, y+1), (x+1, y), (x, y-1)):
            if (-1<nx<N) and (-1<ny<N):
                x = tf[A[nx][ny]] + d
                if dp[nx][ny] > x:
                    dp[nx][ny] = x
                    heappush(q, (x, nx, ny))
    return dp[-1][-1]  # 최종 도착지의 값 반환


ans = []
INF = 10**5
tf = {str(i): i for i in range(0, 10)}  # 변환 딕셔너리(str(숫자) => int(숫자))
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = [tuple(input()) for _ in range(N)]
    ans.append('#{} {}'.format(tc, dijkstra(0, 0)))

print(*ans, sep='\n')
