import copy
for tc in range(1, 11):
    t = int(input())
    maze = []
    for _ in range(16):
        maze.append(list(input()))
    temp = copy.deepcopy(maze)
    result = 0              # 길 있는지 여부
    r, c = 1, 1
    for _ in range(512):
        if maze[r][c + 1] == '3':
            result = 1
            break
        elif maze[r - 1][c] == '3':
            result = 1
            break
        elif maze[r + 1][c] == '3':
            result = 1
            break
        else:
            if (maze[r + 1][c] == '1') and (maze[r][c + 1] == '0' or maze[r][c + 1] == "2"):         # 오른쪽에 벽이 있고 앞에 길이 있는 경우
                c = c + 1
            elif (maze[r + 1][c] == '0') and (maze[r + 1][c - 1] == '1'):   # 세갈래길인데 이전 길 오른쪽에 벽이 있는 경우
                r = r + 1
                r, c = 16 - 1 - c, r
                for a in range(16):
                    for b in range(16):
                        maze[a][b] = temp[b][16 - 1 - a]
            else:
                if (maze[r - 1][c] == '0'):
                    r = r - 1
                r, c = c, 16 - 1 - r
                for a in range(16):
                    for b in range(16):
                        maze[a][b] = temp[16 - 1 - b][a]
            temp = copy.deepcopy(maze)
    print(" #{} {}".format(tc, result))