import sys
sys.stdin = open('input.txt')

T = int(input())

def find(x,y,z):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    global ans
    for k in range(4):
        new_x = x + dx[k]
        new_y = y + dy[k]
        if 0 <= new_x < N and 0 <= new_y < N and visit[new_y][new_x] == 0 and maze[new_y][new_x] == 0:
            visit[new_y][new_x] = 1
            find(new_x,new_y,z+1)
        elif 0 <= new_x < N and 0 <= new_y < N and maze[new_y][new_x] == 3:
            if ans > z:
                ans = z

for i in range(T):
    maze = []
    N = int(input())
    for _ in range(N):
        maze.append(list(map(int,input())))
    visit = [[0]*N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if maze[y][x] == 1:
                visit[y][x] = 1
    for x in range(N):
        for y in range(N):
            if maze[y][x] == 2:
                start_x = x
                start_y = y
    ans = 5555
    z = 0
    find(start_x,start_y,0)
    if ans == 5555:
        ans = 0

    print('#{} {}'.format(i+1,ans))