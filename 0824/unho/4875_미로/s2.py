'''
recursion
'''

import sys
sys.setrecursionlimit(15000)
sys.stdin = open('input.txt')



def recursive_dfs(i, j):
    global answer

    # Base Case
    if maze[i][j] == '3':
        answer = 1
        return

    else:
        for k in range(4):
            y = i + dr[k]
            x = j + dc[k]

            if 0 <= x < N and 0 <= y < N and maze[y][x] != '1' and not visited[y][x]:
                visited[i][j] = True
                recursive_dfs(y, x)



dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


test_case = int(input())

for tc in range(1, test_case+1):
    N = int(input())
    sign = False
    visited = [[False]*N for _ in range(N)]
    answer = 0

    maze = [input() for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                visited[i][j] = True
                recursive_dfs(i, j)
                sign = True
                break
        if sign:
            break

    print('#{} {}'.format(tc, answer))