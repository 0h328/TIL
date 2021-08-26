import sys

sys.stdin = open('input.txt')

# 핵심은 거리가 나아가는 노드가 현재 노드에서 +1이되는것
# distance 를 방문 확인용과 방문용으로 합쳐서 쓸수 있다. 나아갈 수 있다는 것은 방문하지 않았다는 것이니깐...
def BFS(start):
    global result
    queu = [start]

    while queu:
        x, y = queu.pop(0)
        # if (x, y) not in visit:
        #     visit.append((x, y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and (data[nx][ny] == 0 or data[nx][ny] == 3) and distance[nx][ny]==0:
                queu.append((nx, ny))
                distance[nx][ny] = distance[x][y] + 1
                if data[nx][ny] == 3:
                    result = distance[x][y]
                    return


for test in range(1, 1 + int(input())):
    N = int(input())

    data = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if data[i][j] == 2:
                x, y = i, j

    start = (x, y)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    result = 0
    distance = [[0] * N for _ in range(N)]
    BFS(start)
    print('#{} {}'.format(test, result))