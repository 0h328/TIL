import sys
sys.stdin = open('input.txt')

def dfs(v):
    list_visit[v] = 1
    for w in list_route[v]:
        if not list_visit[w]:
            dfs(w)

for i in range(10):
    a,b = input().split()
    a,b = int(a), int(b)
    nums = list(map(int,input().split()))
    list_route = [[] for _ in range(100)]
    list_visit = [[] for _ in range(100)]
    for k in range(len(nums)-1):
        if k % 2 == 0:
            list_route[nums[k]].append(nums[k+1])
    dfs(0)
    if list_visit[99] == 1:
        print('#{} {}'.format(i+1,1))
    else:
        print('#{} {}'.format(i + 1,0))
