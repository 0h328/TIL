import sys
sys.stdin = open('input.txt')

def dfs(number, success):
    global ans
    if number == N:
        if ans < success:
            print(res)
            ans = success
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            res.append(data[number][i])
            dfs(number + 1, success * data[number][i])
            res.pop()
            visited[i] = 0

T = int(input())

def minus(num):
    num = int(num) / 100
    return float(num)

for case in range(1):
    N = int(input())
    data = [list(map(minus, input().split())) for _ in range(N)]
    visited = [0] * N
    ans = 0
    res = []
    dfs(0, 1)
    print('#{} {:.6f}'.format(case + 1, round(ans * 100, 7)))