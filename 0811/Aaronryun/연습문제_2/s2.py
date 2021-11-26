import sys

sys.stdin = open('input2.txt')

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for test in range(T):
    num = int(input())
    data = [list(map(int,input().split())) for _ in range(num)]
    x,y = 0,0
    ans = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            for h in range(4):
                nx = i + dx[h]
                ny = j + dy[h]
                if 0<=nx<num and 0<=ny<num:
                    ans += abs(data[i][j]-data[nx][ny])
    print(ans)

