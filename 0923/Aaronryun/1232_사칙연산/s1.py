import sys

sys.stdin = open('input.txt')


def solve(data, start):
    operator, node1, node2 = data.get(start) # 분리
    node1, node2 = int(node1), int(node2) # 인트화

    if len(data[node1]) != 1: # 마지막으로 갈 수 있는 곳까지
        node1 = solve(data, node1)
    else:
        node1 = int(data.get(node1)[0]) # 도착하면 그 값이 노드

    # 오른쪽 반복
    if len(data[node2]) != 1:
        node2 = solve(data, node2)
    else:
        node2 = int(data.get(node2)[0])

    if operator == '+':
        return node1 + node2
    elif operator == '-':
        return node1 - node2
    elif operator == '*':
        return node1 * node2
    else:
        return node1 // node2


for test in range(1, 11):
    N = int(input())
    data = {}
    for _ in range(N):
        temp = list(input().split())
        data[int(temp[0])] = temp[1:]

    answer = solve(data, 1)
    print('#{} {}'.format(test, answer))
