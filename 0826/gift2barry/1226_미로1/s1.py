import sys
sys.stdin = open('input.txt')

# thought process:
# 큐와 visited 생성,
# 접근 가능한 정점이 있으면 큐에 넣자,
# 해당 정점으로 이동,
# 이동할 때 마다 visited체크와 주변 이동 가능 정점을 인큐
# 이동 지점에 도달 할 때마다 디큐
# bfs 는 돌아올 필요가 없으니, visited 필요 없지 않을까, 하지만 중복 없애기 위해 일단 써보자
# 2차원 배열이 아닌, 2차원 문자열임을 기억

# 팁: 있는지없는지만 확인할떄는 set 타입이 훨씬 효율적

for tc in range(1, 11):
    T = int(input())

    maze = [list(map(int, *input().split())) for _ in range(16)]     # 미로 생성
    v = [[0]*16 for _ in range(16)]                                  # 방문기록표 생성

    Q = []                              # 큐 생성
    x, y = 0, 0
    for i in range(16*16):                 # 시작 위치 확인
        r, c = divmod(i, 16)            # divmod() : 목과 나머지 반환해줌
        # for j in range(16):
        #     if maze[r][c] == 2:
        #         x, y = r, c           # 시작위치 지정 오리지널 방법
        #         break
        if maze[r][c] == 2:
            x, y = r, c  # 시작위치 지정
            break

    Q.append([x, y])                    # 시작위치 인큐

        # 상  우 하 좌
    dr = [-1, 0, 1, 0]                  # 델타 값 생성
    dc = [0, 1, 0, -1]
    ans = 0
    nx, ny = 0, 0
    while Q:                            # 방문할 위치가 없어질 때 까지
        coord = Q.pop(0)                # 시작위치 디큐해서 스타트
        v[coord[0]][coord[1]] = 1       # 방문 체크
        for i in range(4):              # 4방 체크
            nx = coord[0] + dr[i]
            ny = coord[1] + dc[i]

            if maze[nx][ny] == 0 and v[nx][ny] == 0:    # 들어갈 수 있으면 인큐
                Q.append([nx, ny])

            elif maze[nx][ny] == 3:                     # 인큐한 위치가 탈출구면
                ans = 1                                 # 1 리턴

    print('#{} {}'.format(tc, ans))                           # 도착하지 못하고 루프가 끝나면, 0 반환
