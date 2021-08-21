import sys
sys.stdin = open('input.txt')

def dfs(v):
    if not visited[v]:
        visited[v] = 1
    if not visited[first[v]]: # first list의 값에 방문한 적 없으면 그 값으로 dfs 돌리기
        dfs(first[v])
    if not visited[second[v]]: # first list의 값을 이미 방문한 적 있다면 second list 값으로 dfs
        dfs(second[v])

for t in range(1, 11):
    C, E = map(int, input().split())
    first = [0] * 100
    second = [0] * 100
    road = list(map(int, input().split()))
    for i in range(E): # first list부터 채워
        if not first[road[i*2]]:
            first[road[i*2]] = road[i*2 + 1]
        else: # 이미 채워져 있다면 second list 채워
            second[road[i*2]] = road[i*2 + 1]
    visited = [0] * 100
    dfs(0)

    if visited[99] == 1:
        print('#{} 1'.format(C))
    else:
        print('#{} 0'.format(C))