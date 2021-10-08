import sys
sys.stdin = open('input.txt')

def find_min(cnt, total):
    global min_result

    if cnt == N:
        if min_result > total:
            min_result = total
            return

    if min_result < total:
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            find_min(cnt+1, total + cost[cnt][i])
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_result = 987654321
    total = 0

    find_min(0, 0)

    print('#{} {}'.format(tc, min_result))
