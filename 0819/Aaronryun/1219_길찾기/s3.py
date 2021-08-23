import sys

sys.stdin = open('input.txt')


def DFS(start): # stack visit 초기화 해주고 하나씩 빼주면서
    stack = [start]
    visited=[]
    while stack:
        node = stack.pop()
        if node == 99:
            return 1
        elif node not in visited:
            visited.append(node)
            stack.extend(graph[node])

    return 0


for test in range(1, 11):
    number, total = map(int, input().split())
    data = list(map(int, input().split()))

    graph = {_: [] for _ in range(100)} # 노드 끝의 최대수+1만큼을 범위로 키값을 초기화

    for i in range(0, len(data), 2): # 받은 좌표값을 2씩 뛰면서 나눠서 저장
        graph[data[i]].append(data[i + 1])

    # print(graph)


    print('#{} {}'.format(test, DFS(0)))
