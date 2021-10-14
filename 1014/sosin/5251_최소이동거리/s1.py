import sys
sys.stdin = open('input.txt')
for T in range(int(input())):
    N, E = map(int, input().split())
    graph = {i:[] for i in range(N+1)}
    for _ in range(E):
        a, b, w = tuple(map(int, input().split()))
        graph[a].append((b, w))
    
    q = [0]
    visited = [1e9]*(N+1)
    visited[0] = 0
    
    while q:
        pos = q.pop()
        for next_pos, weight in graph[pos]:
            if visited[next_pos]!=1e9:
                temp = visited[next_pos]
                visited[next_pos] = min(visited[next_pos], visited[pos]+weight)
                if temp == visited[next_pos]:
                    continue
            else:
                visited[next_pos] = visited[pos]+weight
            q.append(next_pos)
    
    print('#{} {}'.format((T+1), visited[N]))

#1 2
#2 4
#3 10