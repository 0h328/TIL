import sys
sys.stdin=open('input.txt')


def dfs(cnt,temp):
    global N, answer
    if temp <= answer:
        return
    if cnt == N:
        answer = max(answer,temp)
        return

    for i in range(N):
        if not visited[i]:
            visited[i]=1
            dfs(cnt+1,temp*data[cnt][i])
            visited[i]=0

for test in range(1,1+int(input())):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            data[i][j]/=100
    visited = [0]*N

    answer = 0
    dfs(0,100)
    print('#{} {:.6f}'.format(test,answer))