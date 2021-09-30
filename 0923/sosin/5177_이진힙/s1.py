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
        parent = i
        while parent//2:
            if graph[parent//2] > graph[parent]:
                graph[parent], graph[parent//2] = graph[parent//2], graph[parent]
            parent//=2

    next_node = N//2
    while next_node:
        result+=graph[next_node]
        next_node//=2

    print('#{} {}'.format((T+1), result))

#1 7
#2 5
#3 65
