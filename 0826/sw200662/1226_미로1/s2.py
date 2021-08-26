import sys
sys.stdin = open('input.txt')

def find(x,y):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    Que = []
    Que.append([x,y])
    visit[y][x] = 1

    while Que:
        x,y = Que.pop()
        for k in range(4):
            mx = x + dx[k]
            my = y + dy[k]
            if visit[my][mx] == 0 and maze[my][mx] == 0:
                visit[my][mx] = visit[y][x] + 1
                Que.append((mx,my))
            elif maze[my][mx] == 3:
                return 1
    return 0




for i in range(10):
    maze = []
    tc = int(input())
    for _ in range(16):
        maze.append(list(map(int,input())))
    visit = [[0]*16 for _ in range(16)]
    for x in range(16):
        for y in range(16):
            if maze[y][x] == 2:
                start_x = x
                start_y = y
    print('#{} {}'.format(i+1,find(start_x,start_y)))