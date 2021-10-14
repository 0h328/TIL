# 문제 푼 시간
import pathlib
import sys
import heapq


sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


def dijkstra():
    q = []
    heapq.heappush(q, (0, 0, 0))
    distance[0][0] = 0

    while q:
        dist, r, c = heapq.heappop(q)

        if r == n-1 and c == n-1:
            return dist

        if distance[r][c] < dist:
            continue

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                h = mp[nr][nc] - mp[r][c]
                h = h if h > 0 else 0
                cost = dist + 1 + h
                if cost < distance[nr][nc]:
                    distance[nr][nc] = cost
                    heapq.heappush(q, (cost, nr, nc))


ans = []
test_case = int(input())

for test in range(1, test_case + 1):
    n = int(input())
    mp = [list(map(int, input().split())) for _ in range(n)]
    distance = [[10**9] * n for _ in range(n)]
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    res = dijkstra()

    ans.append("#{} {}".format(test, res))

print(*ans, sep="\n")
