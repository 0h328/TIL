# 문제 푼 시간
import pathlib
import sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


ans = []
test_case = int(input())

for test in range(1, test_case + 1):
    n = int(input())
    mp = [list(map(int, input().split())) for _ in range(n)]
    t = (n**2+1)
    visited = [0]*t
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    res = [1, 1]

    for r in range(n):
        for c in range(n):
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < n and 0 <= nc < n:
                    if mp[r][c] == mp[nr][nc] + 1:
                        visited[mp[r][c]] = 1

    chk = cnt = 1
    for i in range(1, t):
        if visited[i]:
            cnt += 1
        else:
            if cnt > res[1]:
                res = [chk, cnt]
            chk = i
            cnt = 1

    if cnt > res[1]:
        res = [chk, cnt]

    ans.append("#{} {} {}".format(test, res[0], res[1]))

print(*ans, sep="\n")
