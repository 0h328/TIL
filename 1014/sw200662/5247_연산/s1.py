import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    que = []
    que.append([N,0])
    visited = set()
    visited.add(N)
    start = -1

    while True:
        start += 1
        n, cnt = que[start]
        if n == M:
            break
        if n + 1 not in visited and n + 1 <= 1000000:
            que.append((n + 1, cnt + 1))
            visited.add(n + 1)
        if n - 1 not in visited and n - 1 <= 1000000:
            que.append((n - 1, cnt + 1))
            visited.add(n - 1)
        if n * 2 not in visited and n * 2 <= 1000000:
            que.append((n * 2, cnt + 1))
            visited.add(n * 2)
        if n - 10 not in visited and n - 10 <= 1000000:
            que.append((n - 10, cnt + 1))
            visited.add(n - 10)
    print('#{} {}'.format(tc,cnt))
