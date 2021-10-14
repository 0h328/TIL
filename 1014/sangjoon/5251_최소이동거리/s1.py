# 문제 푼 시간
import pathlib
import sys

from collections import defaultdict
import heapq


sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


def dijkstra():
    q = []
    heapq.heappush(q, (0, 0))
    distance[0] = 0

    while q:
        dist, s = heapq.heappop(q)

        if s == N:
            return dist

        if distance[s] < dist:
            continue

        for e, w in tree[s]:
            cost = dist + w
            if cost < distance[e]:
                distance[e] = cost
                heapq.heappush(q, (cost, e))


ans = []
test_case = int(input())

for test in range(1, test_case + 1):
    N, E = map(int, input().split())

    tree = defaultdict(set)
    for _ in range(E):
        s, e, w = map(int, input().split())
        tree[s].add((e, w))

    distance = [float("inf")]*(N+1)
    res = dijkstra()

    ans.append("#{} {}".format(test, res))

print(*ans, sep="\n")
