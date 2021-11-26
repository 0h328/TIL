import sys

sys.stdin = open('input.txt')

def check(y, x):
    return 0 <= y < N and 0 <= x < N

def DFS(y, x):
    stack = [(y, x)]
    visit = []

    while stack: # 스택이 존재하는 동안
        y, x = stack.pop() # 첫 좌표를 뽑아서
        if (y, x) not in visit: # 방문지에 넣고
            visit.append((y, x))

            for i in range(4): # 상하좌우를 돌면서
                ny = y + dy[i]
                nx = x + dx[i]

                if check(ny, nx): # 범위내에 존재하고
                    if data[ny][nx] == 3: # 도착지에 도착하면
                        return 1 # 1
                    elif data[ny][nx] == 0: # 갈수있는 곳이면
                        stack.append((ny, nx)) # 스택에 추가해서 이동
    return 0


for test in range(1, 1 + int(input())):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(N):
        for j in range(N):
            if data[i][j] == 2:
                y, x = i, j

    print('#{} {}'.format(test, DFS(y, x)))
