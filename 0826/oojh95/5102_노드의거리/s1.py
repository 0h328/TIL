import sys
sys.stdin = open('input.txt')

def bfs(s):
    global result
    Q.append(s)
    visited[s] = 1

    while Q:
        s = Q.pop(0)
        for i in range(1, V+1):
            if num[s][i] and not visited[i]:
                Q.append(i)
                visited[i] = 1
                distance[i] = distance[s] + 1
                if i == G:
                    result = distance[i]
                    return
    return

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    num = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        num[s][e] = 1
        num[e][s] = 1
    print(num)
    S, G = map(int, input().split())

    visited = [0] * (V+1)
    distance = [0] * (V+1)
    Q = []
    result = 0
    bfs(S)
    print('#{} {}'.format(tc, result))