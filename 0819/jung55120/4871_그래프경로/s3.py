import sys
sys.stdin = open('input.txt')

def dfs(start, end):
    stack = [start]
    while stack:
        v = stack.pop(0)
        if not visit[v]:
            visit[v] = 1
            for i in node_list:
                if i[0] == v:
                    stack.append(i[1])
        else:
            pass

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    # print(V, E)
    node_list = []
    for _ in range(E):
        start, end = map(int, input().split())
        node_list.append([start, end])
    visit = [0] * (V+1)
    S, G = map(int, input().split())

    dfs(S, G)
    if visit[G]:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))

