def BFS(y, x):  # y, x = 1, 1

    Q = []
    Q.append((y, x))    # Q에 시작점 삽입
    visited[y][x] = 1   # 시작점 방문 체크

    while Q:    # Q가 비어있지 않은 경우
        yi, xi = Q.pop(0)    # Q의 첫번째 요소 삭제하고
        visited[yi][xi] = 1  # 방문 체크

        for i in range(4):   # 첫번째 요소와의 인접점 구하자
            ny, nx = yi + dy[i], xi + dx[i]

            if 0 <= ny < 16 and 0 <= nx < 16:   # 인접점이 정상 범위 내에 있고

                if not maze[ny][nx] and not visited[ny][nx]:    # 길이면서(0) & 방문하지 않았다면
                    Q.append((ny, nx))      # Q에 추가

                elif maze[ny][nx] == 3:     # 인접점이 도착지점이라면
                    return 1                # 탐색 종료
    return 0    # 끝까지 3을 찾지 못하면 실패


import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    visited = [[0]*16 for _ in range(16)]
    dy = [0, 1, 0, -1]  # 우, 하, 좌, 상
    dx = [1, 0, -1, 0]
    for y in range(16):
        for x in range(16):
            if maze[y][x] == 2:
                start_y, start_x = y, x

    print('#{} {}'.format(tc, BFS(start_y, start_x)))