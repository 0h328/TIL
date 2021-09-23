import sys
sys.stdin = open('input.txt')

def lrv(node):
    if len(graph[node]) < 3:
        return int(graph[node][1])
    else:
        if graph[node][1] == '+':
            return lrv(graph[node][2]) + lrv(graph[node][3])
        elif graph[node][1] == '-':
            return lrv(graph[node][2]) - lrv(graph[node][3])
        elif graph[node][1] == '*':
            return lrv(graph[node][2]) * lrv(graph[node][3])
        elif graph[node][1] == '/':
            return lrv(graph[node][2]) / lrv(graph[node][3])

for T in range(10):
    N = int(input())
    graph = {str(i) : input().split() for i in range(1, N+1)}

    result = int(lrv('1'))
    
    print('#{} {}'.format((T+1), result))

#1 13
#2 20
#3 35
#4 107
#5 369
#6 76
#7 123
#8 313
#9 238
#10 2