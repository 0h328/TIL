import sys
from collections import deque
sys.stdin = open('input.txt')


def bfs(l, l2, l3):
    q = deque()
    visited = [[0] * n for _ in range(n)]
    res = 0
    if len(l2) == 1 and len(l3) == 1:
        q.append((l2[0], l[l2[0]].index(2)))
        visited[l2[0]][l[l2[0]].index(2)] = 1
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if -1 < nx < n and -1 < ny < n and visited[nx][ny] == 0:
                    if l[nx][ny] == 3:
                        res = 1
                        visited[nx][ny] = 1
                        return res
                    elif l[nx][ny] == 0:
                        visited[nx][ny] = 1
                        q.append((nx, ny))
    else:
        res = 'error'
    return res


t = int(input())
for idx in range(1, t+1):
    n = int(input())
    l, list2, list3 = [], [], []
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    for i in range(n):
        sub = [int(j) for j in input()]
        if 2 in sub:
            list2.append(i)
        if 3 in sub:
            list3.append(i)
        l.append(sub)

    print('#{} {}'.format(idx, bfs(l, list2, list3)))





