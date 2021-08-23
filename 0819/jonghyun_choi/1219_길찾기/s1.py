import sys
sys.stdin = open('input.txt')

def dfs(start):
    stack = [start]

    while stack:
        v = stack.pop()

        if not visited[v]:
            visited[v] = 1

            for w in range(100):
                if G[v][w] == 1 and not visited[w]:
                    stack.append(w)



for _ in range(10):
    N, length = map(int, input().split())
    G = [[0 for _ in range(100)] for _ in range(100)]
    data_list = list(map(int,input().split()))
    for i in range(length):
        G[data_list[i * 2]][data_list[i * 2 + 1]] = 1
    visited = [0] * 100

    dfs(0)

    if visited[99] == 0:
        print('#{} {}'.format(N, 0))
    else:
        print('#{} {}'.format(N, 1))
