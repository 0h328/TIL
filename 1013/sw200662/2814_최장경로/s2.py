import sys

sys.stdin = open('input.txt')

T = int(input())

def dfs(idx,cnt):
    global ans
    visit[idx] = 1
    if cnt > ans:
        ans = cnt
    for i in num_list[idx]:
        if not visit[i]:
            dfs(i,cnt+1)
            visit[i] = 0

for tc in range(1, T + 1):
    N,M = map(int,input().split())
    num_list =[[] for i in range(N+1)]
    for i in range(M):
        X,Y = map(int,input().split())
        num_list[X].append(Y)
        num_list[Y].append(X)
    ans = 0

    for i in range(1,N+1):
        visit = [0] * (N+1)
        dfs(i,1)
    print('#{} {}'.format(tc,ans))
