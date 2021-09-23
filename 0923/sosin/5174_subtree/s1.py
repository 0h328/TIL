import sys
sys.stdin = open('input.txt')

for T in range(int(input())):
    result = 0
    E, target = map(int, input().split())
    N = E+1
    data = list(map(int, input().split()))
    graph = {i:[] for i in range(N+1)}
    for i in range(len(data)//2):
        graph[data[2*i]].append(data[2*i+1])
    
    stack = [target]
    while stack:
        next_node = stack.pop()
        result+=1
        for n in graph[next_node]:
            stack.append(n)
    print('#{} {}'.format((T+1), result))

#1 3
#2 1
#3 3
