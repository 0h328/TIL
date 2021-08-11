import sys

sys.stdin = open("input.txt")

test_case = int(input())

for test in range(1, test_case + 1):
    n = int(input())
    ans = [[0] * n for _ in range(n)]
    dr = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    num, cnt, check, = (
        1,
        n,
        0,
    )
    cnt = n
    x, y = -1, 0

    while cnt:

        if check % 2:
            cnt -= 1

        for i in range(cnt):
            x += dr[check % 4][0]
            y += dr[check % 4][1]
            ans[y][x] = num
            num += 1

        check += 1

    print("#{}".format(test))
    for row in ans:
        for num in row:
            print(num, end=" ")
        print()
