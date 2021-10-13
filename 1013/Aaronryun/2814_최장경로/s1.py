import sys
sys.stdin=open('input.txt')

def dfs(start,cnt):
    global answer
    visit[start]=1
    cnt +=1
    if answer < cnt:
        answer = cnt

    for i in graph[start]:
        if not visit[i]:
            dfs(i,cnt)
    visit[start]=0

    # stack = [start]
    # visit = []
    # while stack:
    #     node = stack.pop()
    #     if node not in visit:
    #         visit.append(node)
    #         stack.extend(graph[node])
    # return visit

for test in range(1,1+int(input())):
    N,M = map(int,input().split())
    graph = {x:[] for x in range(N+1)}
    answer = 0
    visit=[0 for _ in range(N+1)]
    for i in range(M):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1,N+1):
        dfs(i,0)


    print('#{} {}'.format(test,answer))