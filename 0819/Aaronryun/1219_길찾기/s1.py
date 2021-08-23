import sys

sys.stdin = open('input.txt')


def DFS(graph, start):
    stack = [start]
    visit = []

    while stack:
        node = stack.pop()
        if node == 99:
            return 1

        elif node not in visit:
            visit.append(node)
            stack.extend(graph[node])

    return 0


for test in range(1, 11):
    number, total = map(int, input().split())
    data = list(map(int, input().split()))

    graph = {x: [] for x in range(100)}
    for i in range(0, len(data), 2):
        graph[data[i]].append(data[i + 1])

    answer = DFS(graph, 0)
    print('#{} {}'.format(number, answer))
    # print(sorted(graph.items()))
