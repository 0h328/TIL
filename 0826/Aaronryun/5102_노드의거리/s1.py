import sys

sys.stdin = open('input.txt')


# 핵심은 노드가 밸류값에 존재하는 노드로 나아갈때 이전 노드까지거리에서 늘어나는것
def BFS():
    queu = [start]
    visit = [0] * (V + 1)
    while queu:
        node = queu.pop(0)
        for i in graph[node]:
            if visit[i] == 0:
                queu.append(i)
                visit[i] = visit[node] + 1
    if visit[end]:
        return visit[end]
    else:
        return 0


for test in range(1, 1 + int(input())):
    V, E = map(int, input().split())

    graph = {x: [] for x in range(V + 1)}

    for i in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    start, end = map(int, input().split())

    answer = BFS()

    print('#{} {}'.format(test, answer))
