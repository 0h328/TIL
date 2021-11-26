import sys
sys.stdin = open('input.txt')


def bfs(n, val):
    Q.append(n)
    i = 0
    while Q:
        tmp = Q.pop(0)
        if tmp < 10:
            break
        if tmp >= val:
            visited[i] = tmp // val
            Q.append(tmp - visited[i]*val)
        else:
            Q.append(tmp)
        if i % 2 == 0:
            val //= 5
        else:
            val //= 2
        i += 1
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    visited = [0] * 8
    Q = []
    bfs(N, 50000)
    print('#{}'.format(tc))
    print(*visited)