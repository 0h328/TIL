import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

for test in range(10):
    test = int(input())
    mp = [list(map(int, input().split())) for _ in range(100)]
    visited = [[0] * 100 for _ in range(100)]
    dx = [1, -1, 0]
    dy = [0, 0, -1]

    r, c = 99, mp[99].index(2)  # 도착지점 부터 출발

    while r > 0:  # 가장 위로 올라왔을 때 종료

        mp[r][c] = 0  # 방문 표시

        for i in range(3):  # 좌우부터 이동가능 확인 이후 위로 이동
            nc = c + dx[i]
            nr = r + dy[i]

            if 0 <= nc < 100 and 0 <= nr < 100 and mp[nr][nc]:  # 이동 가능 확인
                if mp[nr][nc]:  # 방문 확인
                    r, c = nr, nc
                    break

    print("#{} {}".format(test, c))