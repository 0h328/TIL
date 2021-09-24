import sys
sys.stdin = open('input.txt')

for T in range(int(input())):
    result = 0
    N = int(input())
    data = tuple(map(int, input().split()))
    graph = {i:0 for i in range(len(data)+1)}

    for i, d in enumerate(data):
        i+=1
        graph[i] = d
        parent = i//2
        while parent:
            if graph[parent] > graph[i]:
                graph[parent], graph[i] = graph[i], graph[parent]
            parent//=2

    next_node = N//2
    while next_node:
        result+=graph[next_node]
        next_node//=2

    print('#{} {}'.format((T+1), result))

#1 7
#2 5
#3 65
