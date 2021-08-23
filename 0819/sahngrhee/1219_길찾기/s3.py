import sys
sys.stdin = open('input.txt')

def DFS(v):
    global ans
    if v == 99:
        ans = 1
        return

    visited[v] = 1

    for w in range(100):
        if not visited[w] and adj_arr[v][w]:
            DFS(w)



for _ in range(10):
    tc, N = map(int, input().split())
    road = list(map(int, input().split()))

    adj_arr = [[0] * 100 for _ in range(100)]

    for i in range(N):
        adj_arr[road[2*i]][road[2*i+1]] = 1

    visited = [0] * 100
    ans = 0
    DFS(0)
    print('#{} {}'.format(tc, ans))