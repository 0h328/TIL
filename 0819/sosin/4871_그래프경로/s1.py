import sys
sys.stdin = open('input.txt')

for T in range(int(input())):
    V, E = map(int, input().split())
    graph = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        graph[s][e] = 1
    
    visited = [0] * (V+1)
    S, G = map(int, input().split())
    stack = [S]
    visited[S] = 1
    result = 0
    while stack:
        pos = stack.pop()
        if pos == G:
            result = 1
            break
        for i, e in enumerate(graph[pos]):
            if e and visited[i]==0:
                visited[i] = 1
                stack.append(i)

    print('#{} {}'.format((T+1), result))

#1 1
#2 1
#3 1
