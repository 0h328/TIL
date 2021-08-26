import sys
sys.stdin = open('input.txt')

def find(x,y):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    global cnt
    for k in range(4):
        new_x = x + dx[k]
        new_y = y + dy[k]
        if visit[new_y][new_x] == 0 and maze[new_y][new_x] == 0:
            visit[new_y][new_x] = 1
            find(new_x,new_y)
        elif maze[new_y][new_x] == 3:
            cnt = 1
            return

for i in range(10):
    maze = []
    tc = int(input())
    for _ in range(16):
        maze.append(list(map(int,input())))
    visit = [[0]*16 for _ in range(16)]
    # for x in range(16):
    #     for y in range(16):
    #         if maze[y][x] == 1:
    #             visit[y][x] = 1
    for x in range(16):
        for y in range(16):
            if maze[y][x] == 2:
                start_x = x
                start_y = y
    cnt = 0
    find(start_x,start_y)
    print('#{} {}'.format(i+1,cnt))