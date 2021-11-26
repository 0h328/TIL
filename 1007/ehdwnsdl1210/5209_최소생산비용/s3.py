# 이건 아니고
def find_cost(n):
    global min_cost
    global cost

    if n == N:
        if min_cost > cost:
            min_cost = cost
        return


    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            cost += factory[n][i]

            if min_cost > cost:
                find_cost(n + 1)


            visited[i] = 0
            cost -= factory[n][i]



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    factory = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N

    min_cost = 987654321

    cost = 0

    find_cost(0)

    print(f'#{tc} {min_cost}')
