# 문제 푼 시간
import pathlib
import sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


def dfs(r, c, num, cnt):
    if cnt == 6:
        set.add(num)

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < 4 and 0 <= nc < 4:
            dfs(nr, nc, num+str[nr][nc], cnt+1)


ans = []
test_case = int(input())

for test in range(1, test_case + 1):
    mp = [list(map(int, input().split())) for _ in range(4)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    res = set()

    for i in range(4):
        for j in range(4):
            dfs(i, j, str(mp[i][j]), 1)

    ans.append("#{} {}".format(test, len(res)))

print(*ans, sep="\n")
