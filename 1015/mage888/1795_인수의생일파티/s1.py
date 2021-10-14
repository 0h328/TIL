import sys
sys.stdin = open('input.txt')

def dijkstra_go(s):
    global dist_go

    for _ in range(N):
        min_idx = -1
        min_val = 99999

        for i in range(1, N+1):
            if not v_go[i] and min_val > dist_go[i]:
                min_idx = i
                min_val = dist_go[i]
        v_go[min_idx] = 1

        for j in range(1, N+1):
            if not v_go[j] and dist_go[j] > dist_go[min_idx] + go[min_idx][j]:
                dist_go[j] = dist_go[min_idx] + go[min_idx][j]

    return dist_go

def dijkstra_back(e):
    global dist_back

    for _ in range(N):
        min_idx = -1
        min_val = 99999

        for i in range(1, N+1):
            if not v_back[i] and min_val > dist_back[i]:
                min_idx = i
                min_val = dist_back[i]
        v_back[min_idx] = 1

        for j in range(1, N+1):
            if not v_back[j] and dist_back[j] > dist_back[min_idx] + back[min_idx][j]:
                dist_back[j] = dist_back[min_idx] + back[min_idx][j]

    return dist_back

T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    go = [[99999 for _ in range(N+1)] for _ in range(N+1)]
    back = [[99999 for _ in range(N+1)] for _ in range(N+1)]
    dist_go = [99999]*(N+1)
    dist_back = [99999]*(N+1)
    v_go = [0]*(N+1)
    v_back = [0]*(N+1)
    dist_go[X] = dist_back[X] = answer = 0

    for _ in range(M):
        x, y, c = map(int, input().split())
        go[x][y] = c
        back[y][x] = c

    dijkstra_go(X)
    dijkstra_back(X)

    for i in range(1, N+1):
        if answer < dist_go[i] + dist_back[i]:
            answer = dist_go[i] + dist_back[i]

    print('#{} {}'.format(tc, answer))




