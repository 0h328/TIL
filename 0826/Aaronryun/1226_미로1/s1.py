import sys

sys.stdin = open('input.txt')

def BFS(y, x):
    queue = [(y, x)]
    visit = []

    while queue: # 큐가 존재하는 동안
        y, x = queue.pop(0) # 첫 좌표를 뽑아서
        if (y, x) not in visit: # 방문지에 넣고
            visit.append((y, x))

            for i in range(4): # 상하좌우를 돌면서
                ny = y + dy[i]
                nx = x + dx[i]

                if 0 <= nx < 16 and 0 <= ny < 16: # 범위내에 존재하고
                    if data[ny][nx] == 3: # 도착지에 도착하면
                        return 1 # 1
                    elif data[ny][nx] == 0: # 갈수있는 곳이면
                        queue.append((ny, nx)) # 스택에 추가해서 이동
    return 0


for test in range(1, 11):
    input()
    data = [list(map(int, input())) for _ in range(16)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    start = (1, 1)
    end = (13, 13)

    print('#{} {}'.format(test,BFS(1, 1)))
