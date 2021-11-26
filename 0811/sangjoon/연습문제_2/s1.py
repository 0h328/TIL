import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

test_case = int(input())

for test in range(1, test_case + 1):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    ans = 0
    for i in range(n):
        for j in range(n):
            r, c = i, j
            cur = lst[r][c]
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]

                if (0 <= nr < n) and (0 <= nc < n):
                    ans += abs(cur - lst[nr][nc])

    print("#{} {}".format(test, ans))