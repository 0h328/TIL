import sys

sys.stdin = open("input.txt")

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c, string, cnt):
    if cnt == 6:
        ans.add(string)
        return

    string += data[r][c]

    for d in range(4):
        nxt_row = r + dr[d]
        nxt_col = c + dc[d]

        if 0 <= nxt_row < 4 and 0 <= nxt_col < 4:
            dfs(nxt_row, nxt_col, string + data[nxt_row][nxt_col], cnt + 1)


T = int(input())

for tc in range(1, T + 1):
    data = [input().split() for _ in range(4)]
    ans = set()

    for row in range(4):
        for col in range(4):
            dfs(row, col, "", 0)

    print("#{} {}".format(tc, len(ans)))
