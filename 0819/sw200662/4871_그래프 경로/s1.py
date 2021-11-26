import sys

sys.stdin = open('input.txt')


def dfs(v):
    list_visit[v] = 1
    for w in list_route[v]:
        if not list_visit[w]:
            dfs(w)


T = int(input())
for i in range(T):
    V, E = map(int, input().split())
    list_route = [[] for _ in range(V + 1)]
    list_visit = [0 for _ in range(V + 1)]
    for k in range(E):
        A, B = map(int, input().split())
        list_route[A].append(B)
    S, G = map(int, input().split())
    dfs(S)
    ans = 1
    if list_visit[G] == 0:
        ans = 0
    print('#{} {}'.format(i + 1, ans))
