import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

test_case = int(input())

for test in range(1, test_case + 1):
    n = int(input())
    red = [[0] * 10 for _ in range(10)]
    blue = [[0] * 10 for _ in range(10)]
    ans = 0

    for _ in range(n):
        r1, c1, r2, c2, color = map(int, input().split())
        if color == 1:
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    red[i][j] = 1

        if color == 2:
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    blue[i][j] = 1

    for i in range(10):
        for j in range(10):
            if red[i][j] == 1 and blue[i][j] == 1:
                ans += 1

    print("#{} {}".format(test, ans))
