import sys
sys.stdin = open('input.txt')

# 7에서 시간 초과

def dfs(idx, cnt):
    global result
    visited[idx] = 1
    if cnt > result:
        return
    if idx == n:
        if result > cnt:
            result = cnt
        return
    for t in tree[idx]:
        if not visited[t[0]]:
            visited[t[0]] = 1
            dfs(t[0], cnt+t[1])
            visited[t[0]] = 0


for tc in range(int(input())):
    n, e = map(int, input().split())
    node_list = [list(map(int, input().split())) for _ in range(e)]
    tree = [[] for _ in range(n+1)]
    for node in node_list:
        tree[node[0]].append((node[1], node[2]))
        tree[node[1]].append((node[0], node[2]))
    result = 1000000
    visited = [0] * (n+1)
    dfs(0, 0)
    print('#{} {}'.format(tc+1, result))
