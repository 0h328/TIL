import sys

sys.stdin = open('input.txt')


def DFS(graph, start):
    stack = [start]
    visit = []

    while stack:
        node = stack.pop()
        if node == end:
            return 1
        elif node not in visit:
            visit.append(node)
            stack.extend(graph[node])

    return 0


for test in range(1, int(input()) + 1):
    V, E = list(map(int, input().split()))

    data = []
    for i in range(E):
        x, y = list(map(int, (input().split())))
        data.append(x)
        data.append(y)
    start, end = list(map(int, input().split()))

    m= max(data)
    graph = {x: [] for x in range(m + 1)}

    for i in range(0, len(data), 2):
        graph[data[i]].append(data[i + 1])

    answer = DFS(graph, start)
    print('#{} {}'.format(test,answer))
