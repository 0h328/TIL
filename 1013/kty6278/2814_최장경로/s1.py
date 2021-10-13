import sys
sys.stdin = open('input.txt')


def dfs(idx):
    global total
    if sum(visited) > total:
        total = sum(visited)
    for i in range(len(tree[idx])):
        if not visited[tree[idx][i]]:
            visited[tree[idx][i]] = 1
            dfs(tree[idx][i])
            visited[tree[idx][i]] = 0

for tc in range(int(input())):
    n, m = map(int, input().split())
    graph_list = [list(map(int, input().split())) for _ in range(m)]
    tree = [[] for _ in range(n+1)]
    for graph in graph_list:
        tree[graph[0]].append(graph[1])
        tree[graph[1]].append(graph[0])
    result = 0
    total = 0
    if n == 1:
        result = 1
    else:
        for i in range(1, n+1):
            visited = [0 for _ in range(n + 1)]
            dfs(i)
            if total > result:
                result = total
    print('#{} {}'.format(tc+1, result))




