import sys
sys.stdin = open('input.txt')

di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]
def dessert_tour(i, j):
    global cnt

    stack = []

    if (i, j) not in visited and not desserts[cafes[i][j]]:
        visited.append((i, j))
        stack.append((i, j))
        desserts[cafes[i][j]] = 1

    if (i, j) == visited[0]:
        cnt += 1
        return

    # while stack:
    stack.pop()
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in visited and not desserts[cafes[ni][nj]]:
            dessert_tour(ni, nj)
            # visited.add((ni, nj))
            # stack.append((ni,nj))
            # desserts[cafes[ni][nj]] = 1
            # i = ni
            # j = nj
        else:
            ni -= di[k]
            nj -= dj[k]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cafes = [list(map(int, input().split())) for _ in range(N)]
    visited = []
    cnt = 0
    desserts = [0 for _ in range(101)]
    print(dessert_tour(0, 0))
    print(cnt)