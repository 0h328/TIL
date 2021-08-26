import sys
sys.stdin = open('input.txt')



def dfs(start):
    stack = [start]

    while stack:
        node = stack.pop()
        if not visited[node[0]][node[1]]:
            visited[node[0]][node[1]] = True

            for k in range(4):
                y = node[0] + dr[k]
                x = node[1] + dc[k]

                if 0 <= y < 16 and 0 <= x < 16 and maze[y][x] != '1':
                    stack.append((y, x))
                    if maze[y][x] == '3':
                        return 1
    return 0


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for _ in range(1, 11):
    tc = int(input())
    maze = [input() for _ in range(16)]
    visited = [[False]*16 for _ in range(16)]
    sign_out = False

    for i in range(16):
        for j in range(16):
            if maze[i][j] == '2':
                start = (i, j)
                sign_out = True
                break
        if sign_out:
            break

    answer = dfs(start)

    print('#{} {}'.format(tc, answer))