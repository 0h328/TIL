import sys
sys.stdin = open('input.txt')

def dfs(visited, battery):
    global ans
    if battery > ans:
        return

    if len(visited) == N:
        battery += road[visited[-1]][0]
        if ans > battery:
            ans = battery
        battery -= road[visited[-1]][0]
        return

    for i in range(N):
        if i not in visited:
            battery += road[visited[-1]][i]
            visited.append(i)
            dfs(visited, battery)
            visited.pop()
            battery -= road[visited[-1]][i]


T = int(input())

for case in range(T):
    N = int(input())
    road = [list(map(int, input().split())) for _ in range(N)]
    ans = 987654321
    dfs([0], 0)

    print('#{} {}'.format(case + 1, ans))