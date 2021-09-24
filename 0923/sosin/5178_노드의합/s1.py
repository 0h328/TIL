import sys
sys.stdin = open('input.txt')

for T in range(int(input())):
    result = 0
    N, E, target = map(int, input().split())
    node_numbers = {}
    for i in range(E):
        temp = tuple(map(int, input().split()))
        node_numbers[temp[0]] = temp[1]

    graph = {i:[i*2, i*2+1] for i in range(N+1)}
    
    stack = [target]
    while stack:
        node = stack.pop()
        for g in graph[node]:
            if g in node_numbers.keys():
                result+=node_numbers.get(g, 0)
            elif g < N+1:
                stack.append(g)

    print('#{} {}'.format((T+1), result))

#1 3
#2 845
#3 1801
