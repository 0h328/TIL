import sys

sys.stdin = open('input.txt')

dx=[0,1,0,-1]
dy=[1,0,-1,0]

T = int(input())

for test in range(T):
    num = int(input())

    n=1
    x,y = 0, -1
    direction = 0

    data = [[0]*num for _ in range(num)]

    while n<=num**2:
        nx,ny = x+dx[direction],y+dy[direction]
        if 0<=nx<num and 0<=ny<num and data[nx][ny] == 0:
            data[nx][ny] = n
            n+=1
            x,y = nx,ny
        else:
            direction = (direction+1)%4

    print('#{}'.format(test+1))
    for i in data:
        for j in range(len(i)):
            print(i[j],end =' ')
        print()