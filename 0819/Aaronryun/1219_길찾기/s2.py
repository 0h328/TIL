import sys

sys.stdin = open('input.txt')


def DFS(start):
    stack = [start]
    visited[start] = True
    while stack:
        node = stack.pop()
        for i in graph[node]:
            if i == 99:
                return 1
            if visited[i] == False:
                stack.append(i)
                visited[i] = True

    return 0


for test in range(1, 11):
    number, total = map(int, input().split())
    data = list(map(int, input().split()))

    graph = {_: [] for _ in range(100)}

    for i in range(0, len(data), 2):
        graph[data[i]].append(data[i + 1])

    # print(graph)

    visited = [False] * (100)

    print('#{} {}'.format(test, DFS(0)))
