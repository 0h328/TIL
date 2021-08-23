import sys
sys.stdin = open('input.txt')

for _ in range(10):
    T, N = input().split()
    graph = {s:[] for s in range(100)}
    roads = tuple(map(int, input().split()))
    for i in range(int(N)):
        graph[roads[i*2]].append(roads[i*2+1])
    visited = [0] * 100
    visited[0] = 1
    stack = [0]
    while stack:
        pos = stack.pop()
        if pos == 99:
            break
        for e in graph[pos]:
            if not visited[e]:
                visited[e] = 1
                stack.append(e)
    print('#{} {}'.format(T, visited[-1]))


#1 1
#2 1
#3 1
#4 0
#5 1
#6 1
#7 0
#8 0
#9 0
#10 0
