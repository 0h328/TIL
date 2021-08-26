import sys
sys.stdin = open('input.txt')


def bfs(S):
    # cnt = 0
    queue = []
    queue.append(S)
    graph[S[0]][S[1]] = -1 # 벽과 구분해주기 위해 음수로 표시

    while queue:
        i, j = queue[0][0], queue[0][1]  # 새 기준점
        queue.pop(0)
        for k in range(4):  # 상하좌우 중 0 인 지점(길)을 queue에 쌓고 1로 변경
            if 0 <= i + di[k] < N and 0 <= j + dj[k] < N:
                if graph[i + di[k]][j + dj[k]] == 0:
                    queue.append((i + di[k], j + dj[k]))
                    graph[i + di[k]][j + dj[k]] = graph[i][j] - 1 # 이전 칸보다 -1
                    # cnt += 1
                elif graph[i + di[k]][j + dj[k]] == 3:
                    graph[i + di[k]][j + dj[k]] = graph[i][j] # 이전 칸과 같게
                    break
            else:
                continue

    if all(3 not in i for i in graph):  # 3이 graph에 안 남아있으면 다 방문한 거
        return abs(graph[E[0]][E[1]]) - 1
    else:  # 남아있으면 루트 끊긴 상태로 종료된 거
        return 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input())) for _ in range(N)]
    # print(graph)

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 2:
                S = (i, j)
            if graph[i][j] == 3:
                E = (i, j)

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    res = bfs(S)
    print('#{} {}'.format(t, res))