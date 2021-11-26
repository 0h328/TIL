import sys
sys.stdin = open('input.txt')

def bfs(start):
    queue = []
    queue.append(start)
    arr[start[0]][start[1]] = 1

    while queue:
        i, j = queue[0][0], queue[0][1] # 새 기준점
        queue.pop(0)
        for k in range(4): # 상하좌우 중 0 인 지점(길)을 queue에 쌓고 1로 변경
            if arr[i + di[k]][j + dj[k]] == 0:
                queue.append((i + di[k], j + dj[k]))
                arr[i + di[k]][j + dj[k]] = 1
            elif arr[i + di[k]][j + dj[k]] == 3: # 3인 지점에 도달하면 값을 1로 변경하고 break
                arr[i + di[k]][j + dj[k]] = 1
                break

    if any(3 in i for i in arr): # 3이 남아있으면 도달하지 못한 것이므로 0
        return 0
    else:
        return 1


for t in range(1, 11):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(16)]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2: # 시작점 찾기
                start = (i, j) # tuple로 넣어줍니다

    res = bfs(start)
    print('#{} {}'.format(t, res))