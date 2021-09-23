import sys
sys.stdin = open('input.txt')

def lvr(node):
    global this_number, result
    if graph[node][0] <= N:
        lvr(graph[node][0])

    result[node] = this_number
    this_number+=1

    if graph[node][1] <= N:
        lvr(graph[node][1])

for T in range(int(input())):
    result = 0
    N = int(input())
    graph = {i:[i*2, i*2+1] for i in range(1, N+1)}
    result = {i:0 for i in range(N+1)}
    this_number = 1
    lvr(1)

    print('#{} {} {}'.format((T+1), result[1], result[N//2]))


#1 4 6
#2 5 2
#3 8 14
