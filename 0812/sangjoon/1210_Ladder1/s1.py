import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

for test in range(10):
    test = int(input())
    mp = [list(map(int, input().split())) for _ in range(100)]
    visited = [[0] * 100 for _ in range(100)]
    dx = [1, -1, 0]
    dy = [0, 0, -1]

    r, c = 99, mp[99].index(2)
    ans = 0

    while r > 0:
        mp[r][c] = 0

        for i in range(2):
            nc = c + dx[i]
            nr = r + dy[i]

            if 0 <= nc < 100 and 0 <= nr < 100:
                if mp[nr][nc]:
                    r, c = nr, nc
                    break
        else:
            r += dy[2]
            c += dx[2]

    print("#{} {}".format(test, c))