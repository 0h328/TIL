import sys
sys.stdin = open('input.txt')

def dfs(now, cnt):
    global res
    if now == 0:
        if cnt < res:
            res = cnt
        return
    elif cnt < res:
        for i in preorder[now]:
            dfs(i, cnt + 1)


t = int(input())
for idx in range(1, t+1):
    info = list(map(int, input().split()))
    m_list = list(map(lambda x: x[0] + x[1], enumerate(info[1:])))
    print(m_list)
    n = info[0]-1
    preorder = [[] for _ in range(n+1)]
    for i in range(n):
        for j in range(i+1, min(n, m_list[i])+1):
            preorder[j].append(i)
    print(preorder)
    res = n
    dfs(n, -1)
    print('#{} {}'.format(idx, res))

