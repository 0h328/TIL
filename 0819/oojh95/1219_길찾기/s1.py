import sys
sys.stdin = open('input.txt')
def dfs(v):
    if not visited[v]:  # 방문하지 않았다면 방문 체크
        visited[v] = 1

    if not visited[arr1[v]]:  # 해당 정점(w)이 정점 v의 인접 정점이고 아직 방문하지 않았다면
        dfs(arr1[v])
    if not visited[arr2[v]]:
        dfs(arr2[v])


for _ in range(10):
    T, L = map(int, input().split())
    arr1 = [0 for _ in range(100)]
    arr2 = [0 for _ in range(100)]
    visited = [0 for _ in range(100)]
    data = list(map(int, input().split()))
    if data.count(99) == 0 or data.count(0) == 0:
        print('#{} 0'.format(T))
    else:
        for i in range(1, L*2, 2):
            if arr1[data[i-1]] == 0:
                arr1[data[i-1]] = data[i]
            else:
                arr2[data[i-1]] = data[i]
        dfs(0)
        if visited[99] == 0:
            print('#{} 0'.format(T))
        else:
            print('#{} 1'.format(T))