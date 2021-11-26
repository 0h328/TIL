# Unsolved
import sys
from pandas import DataFrame

sys.stdin = open('input.txt')


def dfs(start):
    stack = [start]

    while stack:
        temp = stack.pop()

        if visited[temp] == 0:
            visited[temp] = 1

            for dest in range(100):
                if G[start][dest] == 1 and visited[dest] == 0:
                    stack.append(dest)




T = 10
test_case = 1
while test_case <= T:
    test_case, E = map(int, input().split())
    edges = list(map(int, input().split()))
    # print(edges)
    visited = [0] * 100
    G = [[0 for _ in range(100)] for _ in range(100)]
    # print(DataFrame(G))

    for i in range(0, len(edges), 2):
        G[edges[i]][edges[i+1]] = 1
    # print(DataFrame(G))

    visited[0] = 1
    dfs(0)

    print('#{0} {1}'.format(test_case, visited[99]))
    # break
    test_case += 1
