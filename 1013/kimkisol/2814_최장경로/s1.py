import sys

sys.stdin = open('input.txt')
'''
N개의 정점과 M개의 간선
가중치가 없는 무방향 그래프
정점의 번호는 1번부터 N번까지 순서대로 부여되어 있다.
경로에는 같은 정점의 번호가 2번 이상 등장할 수 없으며, 경로 상의 인접한 점들 사이에는 반드시 두 정점을 연결하는 간선이 존재해야 한다.
경로의 길이는 경로 상에 등장하는 정점의 개수를 나타낸다.
그래프에서의 최장 경로의 길이를 출력
'''


def dfs(node, length):
    global max_res

    if length > max_res:
        max_res = length

    for i in tree[node]:
        if not visited[i]:
            visited[node] = 1
            dfs(i, length + 1)
            visited[node] = 0


T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())  # N: 정점 수, M: 간선 수
    tree = [[] for _ in range(N + 1)]
    max_res = 1

    for _ in range(M):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    for i in range(1, N + 1):
        visited = [0] * (N + 1)
        visited[i] = 1
        dfs(i, 1)
        visited[i] = 0
        if max_res == N:
            break

    print('#{} {}'.format(t, max_res))
